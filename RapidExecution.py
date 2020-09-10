import os
class RapidExecution:
    def __init__(self,text):
        self.Main(text)
    def Main(self,text):
        mainString=''
        funcName=""
        parametersExist =True 
        text_stripped =text.strip()
        defString=text_stripped[0:3]
        if defString!="def" :
            return    
        text_stripped=text_stripped[3:]
        text_stripped =text_stripped.strip()
        for char in text_stripped:
            if char != '(' :
                funcName+=char
            else:
                break
        funcName=funcName.strip()
        mainFile=open("Function.py","w+")
        mainFile.write(text)
        mainFile.close()
        mainString+="import Function\n"
        mainString+='if __name__ == "__main__":\n'
        
        text_stripped=text_stripped[len(funcName):]
        text_stripped =text_stripped.strip()
        text_stripped=text_stripped[1:]    
        
        closingBracketIndex = 0

        for char in text_stripped:
            if char != ')' :
                closingBracketIndex= closingBracketIndex+1
            else:
                break
        
        parameters=text_stripped[0:closingBracketIndex]
        parameters=parameters.split(',')
        if parameters[0].strip()=='':
            parametersExist=False
        if parametersExist:
            for i,parameter in enumerate(parameters):
                parameter=parameter.strip()
                parameters[i]=parameter
                mainString+='\t{} = (input("Please enter the value of {}: " ))\n'.format(parameter,parameter)
        mainString+='\tFunction.{}('.format(funcName)
        for parameter in parameters:
            mainString+='{}, '.format(parameter)
        mainString=mainString[0:len(mainString)-2]
        mainString+=')'
        mainFile=open("RapidExecutionmain.py","w+")
        mainFile.write(mainString)
        mainFile.close()
        os.system('python RapidExecutionmain.py')
