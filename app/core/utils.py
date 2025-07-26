from passlib.context import CryptContext
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

hash_password = lambda pwd: pwd_context.hash(pwd)
verify_password = lambda plain, hashed: pwd_context.verify(plain, hashed)
now =  lambda: datetime.utcnow()