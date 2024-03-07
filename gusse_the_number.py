from random import randint
def generate_number():
    randome_Number=randint(0,10)
    return randome_Number
i=1
def main():
    the_Number=generate_number()
    
    while True:
        print('Gusse the number')
        
        number=input()
        
        try:
            number= int(number)
        except:
            print("wrong number")  
            continue    
        if number==the_Number:
            print('cungres  '+str(i))
            break
        elif number > the_Number:
            print('go lower')
        elif number < the_Number:
            print('go higher')
        print("========================")
        i+=1
main() 
