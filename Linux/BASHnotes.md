#Reference used: https://www.youtube.com/watch?v=e7BufAVwDiM

1. Hello Bash Scripting:
  touch helloScript.sh
  To run from terminal: ./helloScript.sh
    MUST BE EXECUTABLE = chmod +x helloScript.sh
    chmod = change mode, +x flag = changing permissions to allow executing file as program
    (Contents of helloScript.sh: 
      #! /bin/bash
      echo "hello bash")
    OUTPUT: hello bash
2. Redirecting to File
  echo "hello bash" > file.txt 
    > takes output and stores it in a file called file.txt, so file.txt would contain only "hello bash"
    >> (double) takes output and APPENDS it to the end of the contents the file already contains
  cat >> file.txt 
    this changes the terminal to an editor where the user can type anything in and have it appended to file.txt
    - USE CTRL+D to exit editor
    - USE CTRL+S to save in text editors (not terminal)
3. Comments
  #(single line comment) = terminal uses this symbol to denote a comment
  : ' comments \n comments \n comments ' (multi-line comments) = terminal uses this notation to denote MANY lines of comments
  cat << var1 (heredocDelimiter (variable name))
  this is a line of text
  and another line
  var1 
  << takes what is listed after the delimiter and outputs it from the terminal
    Using the delimiter at the end ends the sequence
    - After running, this script spits what was written in the file out of the terminal
    OUTPUT: this is a line of text
             and another line
4. Conditional Statements
  count=10 #integer variable of 10
  if [ $count -eq 10 ] #conditional statement that checks if the variable has an equal value to the listed
    #if statements need brackets [] and need spaces between what they encompass
  then #what happens if the condition is true
      echo "the condition is true"
   fi #this is what denotes the end of an if statement
    OUTPUT: the condition is true
   if it were false, nothing would happen, so if we want something to happen, we need an 'else' statement after the 'then' block
   -eq is a comparator (equal to)
   -ne is a comparator (not equal to)
   -gt is a comparator (greater than)
   You can also use an < or > but you must replace [ ] with (( ))
   You can use elif for multiple conditions
   && is used as logical AND
