#include <stdio.h>
#include <string.h>

int my_printf(char *format_string, char *param){
	for(int i=0;i<strlen(format_string);i++){
		if(format_string[i]!='#'){
			putchar(format_string[i]);
			continue;
		}
		if((format_string[i] == '#') && (format_string[i+1] == 'g')){
			i++;
			int lenght1,temp;
			lenght1 = strlen(format_string);
			for(int i = 0;i<lenght1/2;i++)
			{
				temp=format_string[i];
				format_string[i]=format_string[lenght1-i-1];
				format_string[lenght1-1-i]=temp;
				printf("%d",format_string[i]);
			}
			
		}else
			putchar(format_string[i]);
	}
	puts("");
	return 0;
}

int main(int argc, char *argv[]){
	char buf[1024],buf2[1024];
	while(gets(buf)){
		gets(buf2);
		my_printf(buf,buf2);
	}
	return 0;
}