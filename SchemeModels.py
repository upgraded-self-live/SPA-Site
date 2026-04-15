import os
import itertools
from sqlmodel import SQLModel, Field
from typing import Optional, List, Dict, Union
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
load_dotenv()
cred = credentials.Certificate(os.getenv("cred_path"))
firebase_admin.initialize_app(cred)
db = firestore.client()  #Gain access to the database and all its collections     
    
def expose_db():
    global db
    return db
class sendEmailSchema(SQLModel): 
    name: str = Field(min_length=10, max_length=100)
    email: str = Field(min_length=10, max_length=100)
    message: str = Field(min_length=10, max_length=1000)

class saveNewsletterSchema(SQLModel):
    email: str = Field(min_length=10, max_length=100)
    
class build_Schema(SQLModel): 
    budget: str
    exp: str
    skinConcerns: str
    skinSensitivity: str
    skinType: str
    time: str
#First I make a function for the ingredients 
#params --skinconcern--, --skin sensitivity-- and --skin type--
def get_recommended_ingredients(DB=db, data:dict={})-> dict:
    try:
        public_collection = DB.collection("Ingredients").limit(5)
        array_map_comparer = []
        
        skin_type = data.get("skinType")
        if skin_type:
            array_map_comparer.append(skin_type)
        
        skin_concern = data.get("skinConcerns")
        if skin_concern:
            array_map_comparer.append(skin_concern)
        
        skin_sensitivity = int(data.get("skinSensitivity"))
        if skin_sensitivity == 3:
            array_map_comparer.append("sensitive")
        #We have to query all in one because chaining queries do not work
        #print(array_map_comparer)
        array_map_comparer = [x for x in array_map_comparer if x and x!= None]
        if array_map_comparer:
            print(array_map_comparer)
            q_result = public_collection.where("best_for","array_contains_any", array_map_comparer).stream()#Creates the query for the ingredients
            result = []
            for q in q_result:
                data = q.to_dict()
                #print(q.id,data,'\n')
                #print(data.get("best_for"))

                if not isinstance(data, dict):
                    print("🚨 BROKEN DOC:", q.id, data, type(data))
                    continue

                result.append({
                    "ingredient_name": q.id,
                    "ingredient_description": data.get('description') or "",
                    "ingredient_best_for": data.get('best_for') or [],
                    "ingredient_disclaimer": data.get('diclaimer') or ""
                })

            return { "status":"complete", "data":result}
        else:
            return compile_return_statment("failed", f"Comparer is of type {type(array_map_comparer)}")
    except Exception as e:
        print(e)
        return compile_return_statment("error", str(e))
#First I will filter products by ingredients 
def get_products_by_ingredients(DB=db,ingredient_list=[],fallback_data={})-> dict:
    public_collection = DB.collection('place_holder_for_product_collection')
    if not ingredient_list or len(ingredient_list) < 2:
        fallback_array = []
        if fallback_data == None:
            return compile_return_statment("failed", "Fallback data is not provided.")
        skin_type = fallback_data.get("skinType")
        if skin_type:
            fallback_array.append(skin_type)
            
        skin_concern = fallback_data.get("skinConcerns")
        if skin_concern:
            fallback_array.append(skin_concern)
        skinsensitivity = int(fallback_data.get("skinSensitivity"))
        if skinsensitivity == 3:
            skinsensitivity = "sensitive"
            fallback_array.append(skinsensitivity)
        fallback_array = [x for x in fallback_array if x]
        fallback_filter = public_collection.where('best_for', "array_contains_any", fallback_array).stream()
        if fallback_filter:
            try:
                return compile_return_statment("complete",[
                    {
                        "product_name": p.id,
                        **p.to_dict()
                    }
                    for p in fallback_filter
                ])
            except Exception as e:
                print(str(e))
                return {"status": "error", "message": str(e)}
    try:
        filter = public_collection.where("ingredients", "array_contains_any", ingredient_list).stream()
        return compile_return_statment("complete",[
                    {
                        "product_name": p.id,
                        **p.to_dict()
                    }
                    for p in filter
                ])
    except Exception as e:
        return compile_return_statment("error", str(e))
    
        
def compile_return_statment(status:str, data: Union[List,dict,str])->dict:
    return {"status": status, "data": data}
#If there is no ingredients I will filter by its 'best_for'
def check_if_email_exists(email: str) -> bool:
    """Check if an email already exists in the Email-List collection"""
    doc_ref = db.collection("Email-List").document(email)
    doc = doc_ref.get()
    return doc.exists

def convert_budget_into_int_array(data:str)->List[Union[int,str]]:
    try:
        s = data.split('_')#separator is an '_'
        print(s)
        return [int(x) for x in s if type(x)== str]
    except:
        return ["none"]

def conjoin_into_sing_array(*args:list)->list:#params=arrays **DEBUG NOTES= This function should only be used to create a singular array from multiple array for querying**
    sing_array:list = []
    try:
        for arr in args:#Loops through the array argument
            for i in arr:
                sing_array.append(i)
    except:
        sing_array = list(itertools.chain(args) )#Fallback method using itertools if the first method fails for some reason
    return sing_array   
       
def set_email_to_coll(email: str) -> Dict[str, dict]:
    try:
        # Check if email already exists (use email as document ID for uniqueness)
        if check_if_email_exists(email):
            return compile_return_statment("failed", f"The email {email} is already in the newsletter list.")

        # Create document with email as the document ID
        doc_ref = db.collection('Email-List').document(email)
        doc_ref.set({"email": email})

        # Verify the document was created
        doc = doc_ref.get()
        if doc.exists:
            return compile_return_statment("success",
                 {
                    "id": doc.id,  # Document ID (which is the email)
                    "email": doc.to_dict().get('email')
            })
        else:
            return compile_return_statment("error", "Failed to create document, because it does not exist.")

    except Exception as e:
        print(e)
        return compile_return_statment("error", str(e))

def get_skincare_steps_v_time_frames(v:List[int])->List[str]:
    return_array = []
     #--List of available steps:
            #Time Frames Skincare steps
            #Under 2 minutes (super quick)
            #•	Cleanser 
            #•	Moisturizer 
            #Goal: Clean + hydrate. Absolute essentials only.
    if v[0] == 1 and v[1] == 2: 
                return_array.append(("cleanser","moisturizer"))
            #________________________________________
            #5–10 minutes (quick & efficient)
            #•	Cleanser 
            #•	Treatment (e.g. acne / hydration / brightening) 
            #•	Moisturizer 
            ##•	SPF (AM only) 
            #Goal: Add one targeted step without overcomplicating.
    if v[0] == 5 and v[1] == 10:
        return_array.append(("cleanser","treatment", "moisturizer","sunscreen"))
            #________________________________________
            #10–20 minutes (enjoy the ritual)
            #•	Cleanser 
            #•	Toner / Essence 
            #•	Treatment (serum) 
            #•	Moisturizer 
            #•	SPF (AM only) 
            #Optional add-ons:
            #•	Eye cream 
            #Goal: Layer hydration + targeted actives for better results.
    if v[0] == 10 and v[1] == 20:
        return_array.append(("cleanser","Toner","treatment", "moisturizer","eye cream","sunscreen"))
            #________________________________________
            #No limit (full dedication)
            #•	Oil cleanser (PM) 
            #•	Water-based cleanser 
            #•	Exfoliant (2–3x per week) 
            #•	Toner / Essence 
            #•	Multiple treatments (e.g. hydrating + active) 
            #•	Eye cream 
            #•	Moisturizer 
            #•	Face oil (optional) 
            #•	SPF (AM only) 
            #Optional add-ons:
            #•	Masks (weekly) 
            #•	Spot treatments 
            #Goal: Fully optimized routine targeting multiple concerns + skin health.
    if v[0] == "none":
        return_array.append(("cleanser","exfoliant","Toner","treatment","eye cream", "mask","moisturizer","sunscreen"))

    return return_array
    