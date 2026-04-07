import os
from sqlmodel import SQLModel, Field
from typing import Optional, List, Dict
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, db, firestore
load_dotenv()
cred = credentials.Certificate(os.getenv("cred_path"))
firebase_admin.initialize_app(cred)
db = firestore.client()  #Gain access to the database and all its collections     
        

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

def check_if_email_exists(email: str) -> bool:
    """Check if an email already exists in the Email-List collection"""
    doc_ref = db.collection("Email-List").document(email)
    doc = doc_ref.get()
    return doc.exists

def set_email_to_coll(email: str) -> Dict[str, dict]:
    try:
        # Check if email already exists (use email as document ID for uniqueness)
        if check_if_email_exists(email):
            return {"status": "Email already exists"}

        # Create document with email as the document ID
        doc_ref = db.collection('Email-List').document(email)
        doc_ref.set({"email": email})

        # Verify the document was created
        doc = doc_ref.get()
        if doc.exists:
            return {
                "status": "Success",
                "data": {
                    "id": doc.id,  # Document ID (which is the email)
                    "email": doc.to_dict().get('email')
                }
            }
        else:
            return {"status": "Error", "error": "Failed to create document"}

    except Exception as e:
        print(e)
        return {"status": "Error", "error": str(e)}


    
    