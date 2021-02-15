//Создайте абстрактный класс утка с методами swim, и  абстрактными методами fly и quack. 

#include <iostream>
using namespace std;

class Duck //инициализируем класс
{
public: static void Swim() //создаём метод для уткоплаванья
{
	cout << "imagine that the duck is swimming on water" << endl; 
}
	  virtual void Quack() = 0; // (пустая) абстрактная функция уткокряканья.
	  virtual void Fly() = 0; // (пустая) абстрактная  функция утколетания.
};
int main()
{
	Duck::Swim(); //вызываем метод уткоплаванья
}
