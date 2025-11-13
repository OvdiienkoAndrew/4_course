#include <iostream>
#include <random>
#include <cmath>
using namespace std;

template <typename T>
T f(const T x)
{
    return x * x * x - 3 * x + 2;
}

template <typename T>
void cap(const T a, const T b, const T eps)
{
    cout << "\nf(x) = x^3 - 3x + 2;\n\n[a,b] = [" << a << "; " << b << "]\n\nε = " << eps << ".\n\n\n";
}

double rand_number_from(const double a, const double b)
{

    double result = 0.0f;

    while (true)
    {

        result = a + ((double)rand() / RAND_MAX) * (b - a);

        if (result != a && result != b)
            return result;
    }
}

double halving_method(const double a, const double b, const double eps)
{
    double lamda_k = 0.00f, nua_k = 0.00f, a_k = a, b_k = b, beta_k = 0.00f;

    int k = 1;
    while (true)
    {
        while (true)
        {
            beta_k = rand_number_from(0, b_k - a_k);
            if (eps > beta_k)
                break;
        }

        lamda_k = (a_k + b_k - beta_k) / 2.0;
        nua_k = (a_k + b_k + beta_k) / 2.0;

        if (f(lamda_k) <= f(nua_k))
            b_k = nua_k;
        else
            a_k = lamda_k;
        cout << "The number of the iteration: " << k << ".\nlambda: f(" << lamda_k << ") = " << f(lamda_k) << ".\nnua: f(" << nua_k << ") = " << f(nua_k) << ".\na:  f(" << a_k << ") = " << f(a_k) << ".\nb:  f(" << b_k << ") = " << f(b_k) << ".\nx: f(" << (a_k + b_k) / 2.0 << ") = " << f((a_k + b_k) / 2.0) << ".\n\n\n";
        k++;
        if (abs(b_k - a_k) < eps)
        {
            return (a_k + b_k) / 2.0;
        }
    }
}

double gold_retin_method(const double a, const double b, const double eps)
{
    double lamda_k = 0.00f, nua_k = 0.00f, a_k = a, b_k = b, beta_k = 0.00f;
    int k = 1;
    while (true)
    {

        lamda_k = a_k + (3 - sqrt(5)) * (b_k - a_k) / 2.0;

        nua_k = a_k + (sqrt(5) - 1) * (b_k - a_k) / 2.0;

        if (f(lamda_k) <= f(nua_k))
            b_k = nua_k;
        else
            a_k = lamda_k;

        cout << "The number of the iteration: " << k << ".\nlambda: f(" << lamda_k << ") = " << f(lamda_k) << ".\nnua: f(" << nua_k << ") = " << f(nua_k) << ".\na:  f(" << a_k << ") = " << f(a_k) << ".\nb:  f(" << b_k << ") = " << f(b_k) << ".\nx: f(" << (a_k + b_k) / 2.0 << ") = " << f((a_k + b_k) / 2.0) << ".\n\n\n";
        k++;
        if (abs(b_k - a_k) < eps)
        {
            if (f(lamda_k) < f(nua_k))
                return lamda_k;
            return nua_k;
        }
    }
}

template <typename T>
T fibonacci(T x)
{
    if (x == 1 || x == 2)
        return 1;

    T last = 1, real = 1, next = 1;

    for (T i = 3; i <= x; ++i)
    {
        next = last + real;

        last = real;

        real = next;
    }

    return real;
}

double fibonacci_method(const double a, const double b, const double eps)
{
    double lamda_k = 0.00f, nua_k = 0.00f, a_k = a, b_k = b;

    unsigned long long int n = 1, k = 1;

    while (true)
    {

        if (fibonacci(n + 1) <= (b - a) / eps && (b - a) / eps <= fibonacci(n + 2))
            break;

        n++;
    }

    while (true)
    {
        lamda_k = a_k + (b_k - a_k) * fibonacci(n - k + 1) / fibonacci(n - k + 3);
        nua_k = a_k + (b_k - a_k) * fibonacci(n - k + 2) / fibonacci(n - k + 3);

        if (f(lamda_k) <= f(nua_k))
            b_k = nua_k;
        else
            a_k = lamda_k;
        cout << "The number of the iteration: " << k << ".\nlambda: f(" << lamda_k << ") = " << f(lamda_k) << ".\nnua: f(" << nua_k << ") = " << f(nua_k) << ".\na:  f(" << a_k << ") = " << f(a_k) << ".\nb:  f(" << b_k << ") = " << f(b_k) << ".\nx: f(" << (a_k + b_k) / 2.0 << ") = " << f((a_k + b_k) / 2.0) << ".\n\n\n";

        if (n == k)
            return (a_k + b_k) / 2.0;

        k++;
    }
}

int main()
{
    double a = 0.00f, b = 2.00f, eps = 1e-4, value = 0;

    srand(time(nullptr));

    cap(a, b, eps);

    value = halving_method(a, b, eps);
    cout << "The Halving method: f_min(" << value << ") = " << f(value) << ".\n\n\n";

    value = gold_retin_method(a, b, eps);
    cout << "The Gold retin method: f_min(" << value << ") = " << f(value) << ".\n\n\n";

    value = fibonacci_method(a, b, eps);
    cout << "The Fibonacci method: f_min(" << value << ") = " << f(value) << ".\n\n\n";

    return 0;
}