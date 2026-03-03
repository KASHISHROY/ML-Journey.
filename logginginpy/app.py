import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger('ArithmeticApp')
def add(a,b):
    result=a+b
    logger.debug(f"The addition is {result}")
    return result
def sub(a,b):
    result=a-b
    logger.debug(f"The subtraction is {result}")
    return result
def mult(a,b):
    result=a*b
    logger.debug(f"The multiplication is {result}")
    return result
def div(a,b):
    result=a/b
    logger.debug(f"The division is {result}")
    return result
add(10,15)
sub(15,10)
mult(2,3)
div(15,3)