#include <stdio.h>
#include <string.h>

void reverse(char*string)
{
	int lenght =strlen(string);
	int middle =lenght/2;
	char temp;
	for(int i=0;i<middle;i++)
	{
		temp=string[i];
		string[i]=string[lenght-i-1];
		string[lenght-i-1]= temp;
	}
}
int my_printf(char *format_string, char *param){
	for(int i=0;i<strlen(format_string);i++){
		if(format_string[i]!='#'){
			putchar(format_string[i]);
			continue;
		}
		if(format_string[i]=='#'&& (format_string[i+1]>'9'&& format_string[i+1]<'0')){
			putchar(format_string[i]);
			continue;
		}
		if(format_string[i]=='#'&& format_string[i+1]>'0'&& format_string[i+1]<'9'&& (format_string[i+2]!='G'|| format_string[i+2]!='g')){
			putchar(format_string[i]);
			continue;
		}
		if(format_string[i]=='#' && (format_string[i+1]!='g'|| format_string[i+1]!='G'))
		{
			putchar(format_string[i]);
			continue;
		}
		if((format_string[i] == '#') && ((format_string[i+1] == 'g')|| format_string[i+1]=='G')){
			i++;
			if(format_string[i]<'0'&& format_string[i]>'9'){
				putchar(format_string[i]);
			}
			else{
			reverse(param);
			printf("%d",param);
			}
		}
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
