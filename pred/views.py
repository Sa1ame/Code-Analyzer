from django.shortcuts import render
from joblib import load
model = load('./savedModels/model.joblib')

# Create your views here.
def pred(request):
    return render(request,'pred.html')
def det1(request):
    return render(request,'det1.html')
def det2(request):
    return render(request,'det2.html')
def det3(request):
    return render(request,'det3.html')
def det4(request):
    return render(request,'det4.html')
def det5(request):
    return render(request,'det5.html')
def det6(request):
    return render(request,'det6.html')
def res1(request):
    Total_number_of_packages = 1 
    Average_cyclomatic_complexity_of_the_methods = 2 
    Cumulative_Halstead_Effort = 2387.44 
    Total_number_of_comment_lines_in_the_system = 0
    Total_number_of_classes = 1
    Cumulative_halstead_length= 49
    Total_cyclomatic_complexity = 2
    Cumulative_Halstead_Volume = 225.48
    Total_number_of_java_statements= 9
    Cumulative_Halstead_Bugs = 0.08
    Maintainabilty_index= 108.34
    Total_Lines_of_code_in_system= 12
    Total_number_of_comments_in_the_system = 0
    Total_number_of_methods= 1 
    Maintainabilty_Index = 108.34

    
    y_pred = model.predict([[Total_number_of_packages, Average_cyclomatic_complexity_of_the_methods, Cumulative_Halstead_Effort, Total_number_of_comment_lines_in_the_system, Total_number_of_classes, Cumulative_halstead_length, Total_cyclomatic_complexity, Cumulative_Halstead_Volume, Total_number_of_java_statements, Cumulative_Halstead_Bugs, Maintainabilty_index, Total_Lines_of_code_in_system, Total_number_of_comments_in_the_system, Total_number_of_methods, Maintainabilty_Index]])
    if y_pred[0] == 0:
        y_pred = 'WRONG'
    elif y_pred[0] == 1:
        y_pred = 'RIGHT'
    
    return render(request,'res1.html', {'result' : y_pred})


def res2(request): 
    Total_number_of_packages = 1 
    Average_cyclomatic_complexity_of_the_methods = 2 
    Cumulative_Halstead_Effort = 10080.71 
    Total_number_of_comment_lines_in_the_system = 0
    Total_number_of_classes = 1
    Cumulative_halstead_length= 123
    Total_cyclomatic_complexity = 2
    Cumulative_Halstead_Volume = 662.59
    Total_number_of_java_statements= 19
    Cumulative_Halstead_Bugs = 0.22
    Maintainabilty_index= 91.31
    Total_Lines_of_code_in_system= 22
    Total_number_of_comments_in_the_system = 0
    Total_number_of_methods= 1 
    Maintainabilty_Index = 91.31

    
    y_pred = model.predict([[Total_number_of_packages, Average_cyclomatic_complexity_of_the_methods, Cumulative_Halstead_Effort, Total_number_of_comment_lines_in_the_system, Total_number_of_classes, Cumulative_halstead_length, Total_cyclomatic_complexity, Cumulative_Halstead_Volume, Total_number_of_java_statements, Cumulative_Halstead_Bugs, Maintainabilty_index, Total_Lines_of_code_in_system, Total_number_of_comments_in_the_system, Total_number_of_methods, Maintainabilty_Index]])
    if y_pred[0] == 0:
        y_pred = 'Wrong'
    elif y_pred[0] == 1:
        y_pred = 'Right'
    
    return render(request,'res2.html', {'result' : y_pred})

def res3(request):
    Total_number_of_packages = 1 
    Average_cyclomatic_complexity_of_the_methods = 4 
    Cumulative_Halstead_Effort = 6213.84
    Total_number_of_comment_lines_in_the_system = 0
    Total_number_of_classes = 1
    Cumulative_halstead_length= 87
    Total_cyclomatic_complexity = 4
    Cumulative_Halstead_Volume = 437.99
    Total_number_of_java_statements= 12
    Cumulative_Halstead_Bugs = 0.15
    Maintainabilty_index= 99.95
    Total_Lines_of_code_in_system= 22
    Total_number_of_comments_in_the_system = 0
    Total_number_of_methods= 1 
    Maintainabilty_Index = 99.95

    
    y_pred = model.predict([[Total_number_of_packages, Average_cyclomatic_complexity_of_the_methods, Cumulative_Halstead_Effort, Total_number_of_comment_lines_in_the_system, Total_number_of_classes, Cumulative_halstead_length, Total_cyclomatic_complexity, Cumulative_Halstead_Volume, Total_number_of_java_statements, Cumulative_Halstead_Bugs, Maintainabilty_index, Total_Lines_of_code_in_system, Total_number_of_comments_in_the_system, Total_number_of_methods, Maintainabilty_Index]])
    if y_pred[0] == 0:
        y_pred = 'Wrong'
    elif y_pred[0] == 1:
        y_pred = 'Right'
    
    return render(request,'res3.html', {'result' : y_pred})


def res4(request):
    Total_number_of_packages = 1 
    Average_cyclomatic_complexity_of_the_methods = 2
    Cumulative_Halstead_Effort = 10060.88
    Total_number_of_comment_lines_in_the_system = 0
    Total_number_of_classes = 1
    Cumulative_halstead_length= 121
    Total_cyclomatic_complexity = 2
    Cumulative_Halstead_Volume = 635.31
    Total_number_of_java_statements= 14
    Cumulative_Halstead_Bugs = 0.21
    Maintainabilty_index= 96.27
    Total_Lines_of_code_in_system= 16
    Total_number_of_comments_in_the_system = 0
    Total_number_of_methods= 1 
    Maintainabilty_Index = 96.27

    
    y_pred = model.predict([[Total_number_of_packages, Average_cyclomatic_complexity_of_the_methods, Cumulative_Halstead_Effort, Total_number_of_comment_lines_in_the_system, Total_number_of_classes, Cumulative_halstead_length, Total_cyclomatic_complexity, Cumulative_Halstead_Volume, Total_number_of_java_statements, Cumulative_Halstead_Bugs, Maintainabilty_index, Total_Lines_of_code_in_system, Total_number_of_comments_in_the_system, Total_number_of_methods, Maintainabilty_Index]])
    if y_pred == 0:
        y_pred = 'Wrong'
    elif y_pred == 1:
        y_pred = 'Right'
    
    return render(request,'res4.html', {'result' : y_pred})


def res5(request):
    Total_number_of_packages = 0 
    Average_cyclomatic_complexity_of_the_methods = 0
    Cumulative_Halstead_Effort = 0
    Total_number_of_comment_lines_in_the_system = 0
    Total_number_of_classes = 0
    Cumulative_halstead_length= 0
    Total_cyclomatic_complexity = 0
    Cumulative_Halstead_Volume = 0
    Total_number_of_java_statements= 0
    Cumulative_Halstead_Bugs = 0
    Maintainabilty_index= 171
    Total_Lines_of_code_in_system= 0
    Total_number_of_comments_in_the_system = 0
    Total_number_of_methods= 0
    Maintainabilty_Index = 171

    
    y_pred = model.predict([[Total_number_of_packages, Average_cyclomatic_complexity_of_the_methods, Cumulative_Halstead_Effort, Total_number_of_comment_lines_in_the_system, Total_number_of_classes, Cumulative_halstead_length, Total_cyclomatic_complexity, Cumulative_Halstead_Volume, Total_number_of_java_statements, Cumulative_Halstead_Bugs, Maintainabilty_index, Total_Lines_of_code_in_system, Total_number_of_comments_in_the_system, Total_number_of_methods, Maintainabilty_Index]])
    if y_pred[0] == 0:
        y_pred = 'Wrong'
    elif y_pred[0] == 1:
        y_pred = 'Right'
    
    return render(request,'res5.html', {'result' : y_pred})

def res6(request):
    Total_number_of_packages = 0 
    Average_cyclomatic_complexity_of_the_methods = 0
    Cumulative_Halstead_Effort = 0
    Total_number_of_comment_lines_in_the_system = 0
    Total_number_of_classes = 0
    Cumulative_halstead_length= 0
    Total_cyclomatic_complexity = 0
    Cumulative_Halstead_Volume = 0
    Total_number_of_java_statements= 0
    Cumulative_Halstead_Bugs = 0
    Maintainabilty_index= 171
    Total_Lines_of_code_in_system= 0
    Total_number_of_comments_in_the_system = 0
    Total_number_of_methods= 0
    Maintainabilty_Index = 171

    
    y_pred = model.predict([[Total_number_of_packages, Average_cyclomatic_complexity_of_the_methods, Cumulative_Halstead_Effort, Total_number_of_comment_lines_in_the_system, Total_number_of_classes, Cumulative_halstead_length, Total_cyclomatic_complexity, Cumulative_Halstead_Volume, Total_number_of_java_statements, Cumulative_Halstead_Bugs, Maintainabilty_index, Total_Lines_of_code_in_system, Total_number_of_comments_in_the_system, Total_number_of_methods, Maintainabilty_Index]])
    if y_pred[0] == 0:
        y_pred = 'Wrong'
    elif y_pred[0] == 1:
        y_pred = 'Right'
    
    return render(request,'res6.html', {'result' : y_pred})

    
    