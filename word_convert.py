# Python3 code to demonstrate working of  
# Convert numeric words to numbers 
# Using join() + split() 
class word_con:
    def word_convertor(self):
        help_dict = { 
            'one': '1', 
            'two': '2', 
            'three': '3', 
            'four': '4', 
            'five': '5', 
            'six': '6', 
            'seven': '7', 
            'eight': '8', 
            'nine': '9', 
            'zero' : '0',
            'eleven' : '11',
            'twelve': '12',
            'thirteen': '13',
            'fourteen':'14',
            'fifteen':'15',
            'sixteen':'16',
            'seventeen':'17',
            'eighteen':'18',
            'nineteen': '19',
            'twenty':'20',
            'thirty':'30',
            'forty':'40',
            'fifty':'50',
            'sixty':'60',
            'seventy': '70',
            'eighty':'80',
            'ninety': '90',
            'hundred':'100',
            'thousand': '1000'
        } 
        
        # initializing string 
        test_str = "one thousand"
        
        # printing original string 
        print("The original string is : " + test_str) 
        
        # Convert numeric words to numbers 
        # Using join() + split() 
        res = ''.join(help_dict[ele] for ele in test_str.split()) 
        #x = test_str.split()
        #print(x)
        
        # printing result  
        print("The string after performing replace : " + res)  

x = word_con()
x.word_convertor()