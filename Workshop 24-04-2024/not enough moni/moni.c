#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void generate_flag(char *buffer) {
    // REDACTED
}

int main() {
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
  unsigned int cash = 1337;
  int choice;
  printf("********************\nWelcome to the shop!\n********************\n");
  while (1) {
    printf("Your balance: %u hackcoins\n", cash);
    printf("What do you want to buy?\n");
    printf(
        "[0] Happiness: 4294967295 hackcoins\n[1] The answer to the ultimate "
        "question of life, the universe, and everything: 4242424242 hackcoins "
        "\n[2] Flag: 31337 hackcoins\n[3] Solution: 250 hackcoins\n[4] "
        "Leave\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    switch (choice) {
    case 0:
      if (cash >= 4294967295) {
        printf("You have succesfully purchased happiness. You happy?\n");
        cash -= 4294967295;
        printf("New balance: %u hackcoins\n", cash);
      } else {
        printf("Not enough money :(\n");
      }
      break;
    case 1:
      if (cash >= 4242424242) {
        printf("The answer to the ultimate question of life, the universe, and "
               "everything is 42.\n");
        cash -= 4242424242;
        printf("New balance: %u hackcoins\n", cash);
      } else {
        printf("Not enough money :(\n");
      }
      break;
    case 2:
      if (cash >= 31337) {
        char flag[64];
        generate_flag(flag);
        printf("Here is your flag: %s", flag);
        exit(0);
      } else {
        printf("Not enough money :(\n");
      }
      break;
    case 3:
      printf("We're all out of solutions. Sorry.\n");
      cash -= 250;
      break;
    case 4:
      exit(0);
    default:
      printf("Invalid choice\n");
    }
    printf("\n");
    sleep(2);
  }
}
