from fastapi import FastAPI, HTTPException, requests, Depends, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi. staticfiles import StaticFiles
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from SchemeModels import sendEmailSchema, saveNewsletterSchema, set_email_to_coll
import smtplib
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
def send_email(xy: sendEmailSchema ,background_task: BackgroundTasks, ):
    print(xy)
    global e_server
    background_task.add_task(Send_Email, e_server, 'support@ugrd.live', f"{xy.name} has an issue.", f"<p> Name: </p> {xy.name}<p>Email: </p> {xy.email}<p>Message: </p>{xy.message}")
    return xy

@app.put('/email/str')
def Store_Email(xy: saveNewsletterSchema, background_task: BackgroundTasks):
    r = set_email_to_coll(xy.email)
    if r.get("status") == "Error": 
        raise HTTPException(status_code=500, detail=r.get("error"))
    if r.get("status") == "Email already exists":
        raise HTTPException(status_code=500, detail=r.get("Status"))
    background_task.add_task(Send_Email, e_server, r.get('data')['email'], "Thank You for Joining",f"<h1 style='color: pink;'>Thank You for Joining Our Newsletter</h1> <p>We will remind you every month of your skincare routine. Don't worry you don't need to answer all the questions again unless you do not purchase the items again after viewing this email.</p> <p>Gotten the results you want? unsubscribe to monthly emails here - </p> <a href='#' target='_blank'>Bye bye 👋</a>")
    return r


app.mount('/assets', StaticFiles(directory='./FrontEnd/dist/assets'), name='assets')
app.mount('/', StaticFiles(directory='./FrontEnd/dist'), name="root")

@app.exception_handler(404)
def SPA_fallback(request:requests, exc):
    return FileResponse('./FrontEnd/dist/index.html')
