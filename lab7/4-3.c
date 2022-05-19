#include <stdio.h>

int main(void)
{
  int x;
  int leftShift, rightShift;

  printf("Enter an integer: ");
  scanf("%d", &x);

  printf("Multiply by two raised to the power: ");
  scanf("%d", &leftShift);
  printf("%d x %d = %d\n", x, 1 << leftShift, x << leftShift);

  printf("Divide by two raised to the power: ");
  scanf("%d", &rightShift);
  printf("%d / %d = %d\n", x, 1 << rightShift, x >> rightShift);

  return 0;
}