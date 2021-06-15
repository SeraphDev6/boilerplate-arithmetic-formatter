from re import search

def arithmetic_arranger(problems,display_answer=False):
  #handle first error condition
  if len(problems)>5:
    return ("Error: Too many problems.")
  list_problems=[]
  problem_lengths=[]
  output=""
  #convert problems to seperated strings and handle other errors
  for p in problems:
    problem = p.split()
    if problem[1]!="+" and problem[1]!="-":
      return("Error: Operator must be '+' or '-'.")
    if len(problem[0])>4 or len(problem[2])>4:
      return("Error: Numbers cannot be more than four digits.")
    if search("[^0-9]",problem[0]) or search("[^0-9]",problem[2]):
      return("Error: Numbers must only contain digits.")
    largest_digit=max(len(problem[0]),len(problem[2]))+1
    list_problems.append(problem)
    #give lengths for each problem
    problem_lengths.append(largest_digit)
  #do this for each problem for first line
  for i in range(len(problems)):
    #add spacing
    for j in range(problem_lengths[i]-len(list_problems[i][0])+1):
      output+=" "
    output+=list_problems[i][0]
    output+="    "
  #remove 4 spaces for testing
  output=output[:-4]
  #line break  
  output+="\n"
  #repeat the same but add in the operator and use the second number
  for i in range(len(problems)):
    output +=list_problems[i][1]
    for j in range(problem_lengths[i]-len(list_problems[i][2])):
      output+=" "
    output+=list_problems[i][2]
    output+="    "
  #remove 4 spaces for testing
  output=output[:-4]
  #line break
  output+="\n"
  #add the dashes
  for i in range(len(problems)):
    for j in range(problem_lengths[i]+1):
      output+="-"
    output+="    "
  #remove 4 spaces for testing
  output=output[:-4]
  #handle display answers
  if display_answer:
    output+="\n"
    for i in range(len(problems)):
      result=0
      if list_problems[i][1] == "+":
        result = int(list_problems[i][0])+int(list_problems[i][2])
      else: 
        result = int(list_problems[i][0])-int(list_problems[i][2])
      for j in range(problem_lengths[i]-len(str(result))+1):
        output+=" "
      output+=str(result)
      output+="    "
    output=output[:-4]
  return output
