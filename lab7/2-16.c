/* echoChar1.c
 * Echoes a character entered by the user.
 * 2017-09-29: Bob Plantz
 */

#include <unistd.h>
//I do not like C, this is not my code, my brain got stuck and looked at their solution
int main(void)
{
  char allLetter [1000]; //this could technically be any length.
                      // if you consider the return character to be the end of a line
                      // a line could be of infinite length
  char* currentPlace = allLetter;                         //keeps current place
                                                          //currently is set to the front of the array because the variable is set to that memory location
  write(STDOUT_FILENO, "Enter one character: ", 21);      // prompt user
  while(*currentPlace!='\n'){                             //if the character at the start of the array is a return character, continue
    currentPlace++;                                       //iterate up one memory location
    read(STDIN_FILENO, currentPlace, 1);                   // one character
  }
  currentPlace = allLetter;                      //set the memory location back to the sart of the array.
  write(STDOUT_FILENO, "You entered: ", 13);         // message
  while(*currentPlace!='\n'){                 //same process
    currentPlace++; 
    write(STDOUT_FILENO, currentPlace, 1);                 // echo character
  }
  return 0; //exit success
}