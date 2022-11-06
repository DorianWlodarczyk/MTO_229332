
#include <stdio.h>
#include <string.h>
#include <ctype.h>

    int my_printf(char *format_string, char *param) {
  



    for (int i = 0; i < strlen(format_string); i++) {
            //jeśli nie występuje "#" to wyświetla 
            if(format_string[i] != '#'){
                putchar(format_string[i]);
                continue;
            }
            //jeśli występuje "#k" bez dlugosci to wyswietla cały string i przy okazji zmienia wielkosc znakow
            if(format_string[i+1]=='k'){
                i++;
                if(param[i]>='a' && param[i]<= 'z'){
                    param[i]=param[i]-32;
                    printf("%s",param);
                    continue;
                }
                else if(param[i]>= 'A' && param[i] <= 'Z'){
                    param[i]=param[i]+32;
                    printf("%s",param);
                    continue;
                }
               
            }
            //jesli jest podane #xk ale x nie jest liczba calkowita
            if(format_string[i]=='#' &&  format_string[i+2]== 'k'){
                if(format_string[i+1]>'9' || format_string[i+1]<'0'){
                    if(param[i]>='a' && param[i]<= 'z'){
                    param[i]=param[i]-32;
                    printf("%s",param);
                    continue;
                }
                else if(param[i]>= 'A' && param[i] <= 'Z'){
                    param[i]=param[i]+32;
                    printf("%s",param);
                    continue;
                }
                    putchar(format_string[i]);
                continue;
                }
                // poprawnie podane dane
                else if(format_string[i+1]>='0' && format_string[i+1]<='9')
                    if(param[i]>='a' && param[i]<= 'z'){
                    param[i]=param[i]-32;
                    printf("%s",param);
                    continue;
                }
                else if(param[i]>= 'A' && param[i] <= 'Z'){
                    param[i]=param[i]+32;
                    printf("%s",param);
                    continue;
                }
            }
           
            
        }

        puts("");
        return 0;

    }

    int main(int argc, char *argv[]) {
        char buf[1024], buf2[1024];
        while (gets(buf)) {
            gets(buf2);
            my_printf(buf, buf2);
        }
        return 0;
    }

