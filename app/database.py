
from prisma import Prisma


prisma = Prisma()  # Create a Prisma client instance

async def connect_db():
     #connect to database before fast api start or will cause error
    await prisma.connect()

async def disconnect_db():
    #disconnect after
    await prisma.disconnect()
