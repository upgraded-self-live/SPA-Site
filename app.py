from fastapi import FastAPI, HTTPException, requests, Depends, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi. staticfiles import StaticFiles
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from SchemeModels import conjoin_into_sing_array, sendEmailSchema, saveNewsletterSchema, set_email_to_coll, build_Schema, get_recommended_ingredients,convert_budget_into_int_array, get_skincare_steps_v_time_frames, expose_db
import smtplib
from starlette import status
import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI(title="UpgradedSelf.live")
e_server = None

origins = [
    "http://localhost:5173",  # Vue dev server
    "http://127.0.0.1:5173",
    "http://127.0.0.1:8000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def MakeHTMLMessage(message: str):
    html_message = f"""
    <html>
        <head>
            <title>UpgradedSelf Newsletter</title>
        </head>
        <body>
            <span></span>
            <p>{message}</p>
            <footer style='display: flex; flex-direction: row; align-items: center; justify-content: space-between; width: 100%; height: 100px; padding: 10px; background-color: pink;'>
                <a href="#" target="_blank">About Us</a>
                <a href="#" target="_blank">Join our Newsletter</a>
                <a href="#" target="_blank">Build your Routine</a>
            </footer>
        </body>
    </html>
    """
    return html_message

def set_up_email_server():
    try:
        server = smtplib.SMTP(os.getenv("SMTP_HOST"), int(os.getenv("SMTP_PORT")))
        server.starttls()
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
        return server
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Failed to set up email server: {str(e)}")
    
def Send_Email(server, recipient_email, subject:str, message:str):
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = os.getenv('SMTP_SENDER_EMAIL')
        msg['To'] = recipient_email
        msg['Subject'] = subject
        html_message =MakeHTMLMessage(message)
        msg.attach(MIMEText(html_message, 'html'))#This attaches as the body could be an html,image or plain text
        server.sendmail(os.getenv('SMTP_SENDER_EMAIL'), recipient_email, msg.as_string())
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create email message: {str(e)}")
    
    
@app.on_event("startup")
def startup_event():
    global e_server
    e_server = set_up_email_server()


@app.post('/mail')
async def send_email(xy: sendEmailSchema ,background_task: BackgroundTasks, ):
    print(xy)
    global e_server
    background_task.add_task(Send_Email, e_server, 'support@ugrd.live', f"{xy.name} has an issue.", f"<p> Name: </p> {xy.name}<p>Email: </p> {xy.email}<p>Message: </p>{xy.message}")
    return xy

@app.put('/email/str')
async def Store_Email(xy: saveNewsletterSchema, background_task: BackgroundTasks):
    r = set_email_to_coll(xy.email)
    if r.get("status") == "Error": 
        raise HTTPException(status_code=500, detail=r.get("error"))
    if r.get("status") == "Email already exists":
        raise HTTPException(status_code=500, detail=r.get("Status"))
    background_task.add_task(Send_Email, e_server, r.get('data')['email'], "Thank You for Joining",f"<h1 style='color: pink;'>Thank You for Joining Our Newsletter</h1> <p>We will remind you every month of your skincare routine. Don't worry you don't need to answer all the questions again unless you do not purchase the items again after viewing this email.</p> <p>Gotten the results you want? unsubscribe to monthly emails here - </p> <a href='#' target='_blank'>Bye bye 👋</a>")
    return r

@app.post('/build')
async def build_routine(skin_data:build_Schema, db = Depends(expose_db))-> dict:
    try:
        if not skin_data:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='INVALID_BODY/INCOMPLETE BODY')
        processable_data = skin_data.model_dump()#Converts the pydantic object to a dictionary for python to understand; **DEBUG NOTES: DO not update in route.**
        mutable_skin_data = processable_data.copy()#Copy of the original dictionary
        
        description_collection = db.collection("description")
        
        budget = processable_data.get("budget")#Get budget
        skin_type = processable_data.get("skinType")#get skin type and use it in a query for getting product
        user_time_willing = processable_data.get("time")
        skin_concern = processable_data.get("skinConcerns")

        description_doc = description_collection.document(skin_type)#Get the description for the skintype from the database
        """cleanser_description, treatment_description, moisturizer_description, spf_description"""
        
        needed_ingredients =get_recommended_ingredients(data = processable_data)
        
            
        #Process the budget data, by spliting by '_'
        budget = convert_budget_into_int_array(budget)
        #Process the time data, by spliting by '_'
        user_time_willing = convert_budget_into_int_array(user_time_willing)
        #Get steps using user_time_willing
        steps_result = get_skincare_steps_v_time_frames(user_time_willing)
        #Loop through the step_result array and make a query as a product type selector
        product_list:list = []
        
        for step in steps_result:
            get_affi_collection = db.collection("Affiliate-Products")
            init_query = get_affi_collection.where("product-type", "==", step)#query via step
            if not needed_ingredients or len(needed_ingredients) == 0:
                init_query = init_query.where("best_for", "array_contains_any", [skin_type, skin_concern])#query using skin type and skin concern if needed ingredientsis empty
            else: 
                init_query = init_query.where("ingredients", "array_contains_any",needed_ingredients)#Query using igredients
            #query via budget
            init_query = init_query.where("price", "<=", budget[len(budget)]) if budget[0] != "none" else init_query.where("price", ">=", 120)#Runs the budget query if the budget first element is not "none"
            init_result = init_query.stream()#Runs the query
            
            if not init_result.to_dict(): #If we cannot find a product from our affiliate database we reference to our products database.
                fall_back_collection = db.collection("Products")
                fallback_query = fall_back_collection.where("product-type", "==", step)#query via step
                if not needed_ingredients or len(needed_ingredients) == 0:
                    fallback_query = fallback_query.where("best_for", "array_contains_any", [skin_type, skin_concern])#query using skin type and skin concern if needed ingredientsis empty
                else: 
                    fallback_query = fallback_query.where("ingredients", "array_contains_any",needed_ingredients)#Query using igredients
                #--query via budget--
                fallback_query = fallback_query.where("price", "<=", budget[len(budget)]) if budget[0] != "none" else fallback_query.where("price", ">=", 120)#Runs the budget query if the budget first element is not "none"
                fallback_result = fallback_query.stream()
                init_result = fallback_result
                if not fallback_result:
                    continue
            result_wrapper = [{
                "product_name": p.id,
                **p.to_dict() 
            }for p in init_result]#Wraps the result in an array for array joining
            product_list = conjoin_into_sing_array(product_list, result_wrapper)#Combines global result to the iterated scope return
        """Wrap the return statement to include description, products and ingredients"""
        #ensure price is between budget during query process
        #Combine the ingredient array with the get_skincare_steps_v_time_frames
        return_dict:dict={
            "steps": len(product_list),
            "a": {},
            "ingredients": needed_ingredients
        }#Data to be sent back 

        #/---- Data Guide----/
        #       "data" : {
        #    "steps": The number of steps gotten from timeframe function,
        #    "a(actions)": "1(cleanser)": {"type": "The current step of the iteration","description": "The skin type step description","products": [array of products with type cleanser],step: 1} 
        #},
        #"ingredients": [dictionary array of ingredients]
        description_doc = description_doc.get().to_dict()#Run the query to fetch the skin type description document
        for step_num,step in enumerate(steps_result):
            return_dict["a"]= {**return_dict.get("a"),(step_num): {"type": step, "description": "", "products": product_list, "step": (step_num+1)}}
            if step =="cleanser":
                return_dict["a"][step_num]["description"] = description_doc.get("cleanser_description")
            if step !="moisturizer" and step !="sunscreen" and step !="cleanser":
                return_dict["a"][step_num]["description"] = description_doc.get("treatment_description")
            if step =="moisturizer":
                return_dict["a"][step_num]["description"] = description_doc.get("moisturizer_description")
            if step =="sunscreen":
                return_dict["a"][step_num]["description"] = description_doc.get("spf_description")
        
        return {"status": "success","data": return_dict}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='BAD_REQUEST')
    

app.mount('/assets', StaticFiles(directory='./FrontEnd/dist/assets'), name='assets')
app.mount('/', StaticFiles(directory='./FrontEnd/dist'), name="root")

@app.exception_handler(404)
def SPA_fallback(request:requests, exc):
    return FileResponse('./FrontEnd/dist/index.html')
