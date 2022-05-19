/* echoDecHex.c
 * Asks user to enter an unsigned integer in decimal and
 * one in hexadecimal then echoes both in both bases.
 * 2017-09-29: Bob Plantz
 */

#include <stdio.h>

int main(void)
{
  unsigned int unsignedInteger;
  unsigned int bitPattern;

  printf("Enter an unsigned decimal integer: ");
  scanf("%u", &unsignedInteger);

  printf("Enter a bit pattern in hexadecimal: ");
  scanf("%x", &bitPattern);

  printf("%u is stored as %#010x, and\n", unsignedInteger, unsignedInteger);
  printf("%#010x represents the unsigned decimal integer %u\n",
             bitPattern, bitPattern);
 //I dont even know, pointers and void pointers and formatting things I found online
  printf("the memory location for the unsignedInteger variable is:%p \nthe memory location for the bit pattern is:%p \n",(void*)&unsignedInteger,(void*)&bitPattern);
  return 0;
}