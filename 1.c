/*
    프로그램 내용: 프로그램2.7에 함수 추가
    작성자: 202010779 송석한
    작성일: 24.03.30
*/
#include <stdio.h>
#define MAX_DEGREE 101

typedef struct{
    int degree;
    float coef[MAX_DEGREE];
} Polynomial;

Polynomial read_poly() {
    int i;
    Polynomial p;

    printf("다항식의 최고 차수를 입력하시오: ");
    scanf("%d", &p.degree);
    printf("각 항의 계수를 입력하시오 (총 %d개): ", p.degree + 1);
    for (i = 0; i <= p.degree; i++)
        scanf("%f", p.coef + i);
    return p;    
}

void print_poly(Polynomial p, char str[]){
    int i;
    printf("\t%s", str);
    for(i = 0; i < p.degree; i++)
        printf("%5.1f x^%d + ", p.coef[i], p.degree - i);
    printf("%4.1f\n", p.coef[p.degree]);    
}

Polynomial add_poly(Polynomial a, Polynomial b){
    int i;
    Polynomial p;
    if (a.degree > b.degree) {
        p = a;
        for(i = 0; i <= b.degree; i++)
            p.coef[i + (p.degree - b.degree)] += b.coef[i];
    }
    else {
        p = b;
        for(i = 0; i <= a.degree; i++)
            p.coef[i + (p.degree - a.degree)] += a.coef[i];
    }
    return p;
}

double Cal_poly(Polynomial p, double x) {
    int i;
    double result = 0.0;
    double x_power = 1.0; // x^0
    for (i = 0; i <= p.degree; i++) {
        result += p.coef[i] * x_power;
        x_power *= x;
    }
    return result;
}

void main() {
    Polynomial a, b, c;
    double x, result;
    
    a = read_poly();
    b = read_poly();
    c = add_poly(a, b);
    
    printf("계산할 x 값을 입력하시오: ");
    scanf("%lf", &x);
    
    result = Cal_poly(a, x);
    printf("A = %.2f\n", result);
    
    result = Cal_poly(b, x);
    printf("B = %.2f\n", result);
    
    result = Cal_poly(c, x);
    printf("A+B = %.2f\n", result);
}
