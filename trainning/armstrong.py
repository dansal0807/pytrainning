#programa que calcula números armstrongs.

import math


COLOR_DEFAULT = "\033[0m"
COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m"
COLOR_YELLOW = "\033[33m"
COLOR_BLUE  = "\033[34m"
COLOR_MAGENTA  = "\033[35m"
COLOR_CYAN  = "\033[36m"
COLOR_LIGHT_GREEN  = "\033[92m"
COLOR_LIGHT_YELLOW  = "\033[93m"
COLOR_LIGHT_BLUE = "\033[94m"
COLOR_LIGHT_MAGENTA = "\033[95m"
COLOR_LIGHT_CYAN = "\033[96m"
   
sum=0
str=f"{COLOR_YELLOW}"
num=input("Para que um número seja armstrong é necessário que a soma das potências de suas partes seja igual ao próprio número.\nEntre com um número: ")
for d in num: #d entra como input, uma string de numeros; d é a quantidade de elementos em num, assim fornece a quantidade digitos.
    p=pow(int(d),len(num))
    print(f"{COLOR_LIGHT_CYAN}O algarismo {d} elevado a {len(num)}º potência ={COLOR_GREEN} {p}")
    str = str + f" {p} +" 
    sum = sum + p
print(f"{COLOR_LIGHT_BLUE}A Soma das Potências:{str[:len(str)-1]}={COLOR_LIGHT_GREEN} {sum}");
if sum==int(num):
    print(f"{COLOR_LIGHT_YELLOW}A soma dos algarismos elevados a {len(num)}º potência é igual a:{COLOR_LIGHT_GREEN} {sum}.{COLOR_LIGHT_YELLOW}\nEsse valor é igual ao próprio número {num}.\nLogo, {COLOR_LIGHT_GREEN}{num} é um número armstrong.{COLOR_DEFAULT}")
else:
    print(f"{COLOR_LIGHT_YELLOW}A soma dos algarismos elevados a {len(num)}º potência é igual a:{COLOR_LIGHT_GREEN} {sum}.{COLOR_LIGHT_YELLOW}\nEsse valor é diferente do próprio número {num}.\nLogo, {COLOR_RED}{num} não é um número armstrong.{COLOR_DEFAULT}")