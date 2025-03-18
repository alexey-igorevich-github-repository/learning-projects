import java.util.Arrays; // импортируем класс Arrays для удобной работы с массивами (из стандартной библиотеки java пакета java.util)
import java.util.Random; // импортируем класс Random для генерации случайных чисел для создания разных полиномов (из стандартной библиотеки java пакета java.util)
import java.util.Scanner; // импортируем класс Scanner для считывания пользовательского ввода с клавиатуры (из стандартной библиотеки java пакета java.util)




public class Polynom { // объявляем класс Polynom - вся программа генерации полиномов завернута в этот класс
    private int dimension;      // переменная для хранения значения степени типа int находящаяся в private scope
    private double[] coefficients; // массив для хранения коэффициентов полинома, хранит значения типа double, находится в private scope
    private static final Random random = new Random(); // создадим объект Random, являющийся экзэмпляром класса Random, не меняющийся внутри класса для генерации случайных чисел

    public Polynom(int dimension, String type, double sparsity) { // создадим конструктор для создания новых объектов типа Polynom
        this.dimension = dimension; // запишем в поле dimension.
        this.coefficients = new double[this.dimension + 1]; // создадим массив coefficients с размером степень+1 (this.dimension + 1). полином степени n имеет n + 1 коэффициентов. нужно добавить единицу. элементы массива будут типа double.
        
        switch (type.toLowerCase()) { // блок switch-case для управления генерацией полинома. приводим пользовательский ввод к нижнему регистру для безопасности
            case "1": // в случае если пользователь ввел цифру 1
                create_regular_polynom(); // вызовем метод create_regular_polynom()
                break; // выходим из блока черех break чтобы не читать дальше
            case "2": // в случае если пользователь ввел цифру 2
                create_symmetric_polynom(); // вызовем метод create_symmetric_polynom()
                break; // выходим из блока черех break чтобы не читать дальше
            case "3": // в случае если пользователь ввел цифру 3
                create_ones_polynom(); // вызовем метод create_ones_polynom()
                break; // выходим из блока черех break чтобы не читать дальше
            case "4": // в случае если пользователь ввел цифру 4
                create_sparse_polynom(sparsity); // вызовем метод create_sparse_polynom()
                break; // выходим из блока черех break чтобы не читать дальше     
            default: // в остальных случаях пользовательского ввода по умолчанию
                create_regular_polynom(); // по умолчанию случайный полином // вызовем метод create_regular_polynom()
        } // конец блока switch-case
    }


    private void create_symmetric_polynom() { // создадим метод create_symmetric_polynom() в private scope, который будет возвращать тип void. для создания симметричного полинома
        for (int i = 0; i <= dimension / 2; i++) { // создадим цикл для заполнения массива коэффициентов именно для симметричного полинома. Проходим только половину массива. вторая половина заполняется зеркально
            double value = random.nextInt(21) - 10; // используем ранее созданный в классе объект random класса Random и с помощью метода nextInt() класса Random сгенерируем случайное число от 0 до 20 [n, n-1], потом отминусуем 10 для смещения диапазона  и получения числа в диапазоне [-10, 10]. запишем полученное число в переменную value типа double.
            this.coefficients[i] = value; // присваиваем значения value начиная слева (с начала массива coefficients). Через i двигаемся по элементам.
            this.coefficients[dimension - i] = value; // присваеваем значения value начиная справа (с конца массива coefficients). через i двигаемся по элементам.
        } // конец цикла for

        if (this.coefficients[this.dimension] == 0) { // создадим условие исправляющее ситуацию, когда коэффициент со старшей степенью оказался равным нулю и полином упал в степени. если коэффицент "старшей степени-степени полинома" == 0, то
            this.coefficients[this.dimension] = random.nextInt(9) + 1; // то тогда присвоим ему рандом int от 1 до 9.
            this.coefficients[0] = this.coefficients[this.dimension]; // Однако не будем забывать что полином должен быть симметричным. Обеспечим зеркалирование
        } // конец условия

    } // конец метода create_symmetric_polynom()


    private void create_regular_polynom() { // создадим метод create_regular_polynom() в private scope, который будет возвращать тип void. для создания обычного полинома
        for (int i = 0; i <= dimension; i++) { // создадим цикл для заполнения массива this.coefficients случайными значениями. цикл будет проходить с 0 до степени полинома включительно.
            this.coefficients[i] = random.nextInt(21) - 10; // Каждую итерацию будем записывать в массив по значению. Чтобы получить отрицательные значения воспользуемся стандартным приемом. попросим числа от 0 до 20, а потом сдвинем диапозон на -10. получим генерацию чисел от -10 до 10.        
            } // закрывающая скобка цикла for

        if (this.coefficients[this.dimension] == 0) { // создадим условие исправляющее ситуацию, когда коэффициент со старшей степенью оказался равным нулю и полином упал в степени. если коэффицент "старшей степени-степени полинома" == 0, то
            this.coefficients[this.dimension] = random.nextInt(9) + 1; // то тогда присвоим ему рандом int от 1 до 9
        } // конец условия
    } // конец метода create_regular_polynom()


    private void create_sparse_polynom(double sparsity) { // создадим метод create_sparse_polynom() в private scope, который будет возвращать тип void. для создания разреженного полинома
        for (int i = 0; i <= dimension; i++) { // создадим цикл, который будет проходить по всем коэфициентам полинома начиная с 0 до dimension вклчително
            if (random.nextDouble() < sparsity) { // условие для сравнения случайного double от 0.0 до 1.0 с заданным double разреженности. условие определения будет ли коэффициент полинома равен 0 или случайным числом
                this.coefficients[i] = random.nextInt(21) - 10; // текущий коэффициент полинома будет случайным числом от -10 до 10
            } else { // во всех остальных случаях
                this.coefficients[i] = 0; // текущий коэффициент полинома будет равен 0
            } // конец условия
        } // конец цикла for
        if (this.coefficients[this.dimension] == 0) { // создадим условие исправляющее ситуацию, когда коэффициент со старшей степенью оказался равным нулю и полином упал в степени. если коэффицент "старшей степени-степени полинома" == 0, то
            this.coefficients[this.dimension] = random.nextInt(9) + 1; // то тогда присвоим ему рандом int от 1 до 9
        }
    }


    private void create_ones_polynom() { // определим метод, который будет создавать единичный полином 
        Arrays.fill(this.coefficients, 1); // заполним весь массив coefficients значениями 1
    } // закрывающая скобка метода  create_ones_polynom()





    public void print_results() { // создадим метод в public scope, который будет возвращать void и нужен для вывода результатов на печать
        StringBuilder sb = new StringBuilder(); // объявим переменную sb которая будет объектом типа StringBuilder и нужна для создания и изменения строк. Главное достоинство что он mutable
        for (int i = dimension; i >= 0; i--) { // задекларируем цикл for, который будет перебирать все коэффициенты полинома от старшего к младшему в порядке убывания
            if (coefficients[i] != 0) { // добавим условие проверку на неравенство коэффициента нулю, в случае если коэффициент равен нулю, то содержимое цикла отработает итерацию вхолостую и ничего в строку не добавится
                if (i != dimension && coefficients[i] > 0) { // условие для правильной расстановки знаков. Если коэффициент не является старшим(первым) и он положительный - то знак +
                    sb.append(" + "); // добавим знак + в объект строки sb
                } else if (coefficients[i] < 0) { // условие для правильной расстановки знаков. в иных случаях знак -
                    sb.append(" - "); // добавим знак - в объект строки sb
                } // закрывающая скобка соответствующего условия if 
                sb.append(Math.abs(coefficients[i])); // теперь добавим в строку коэффициент. По модулю, потому что нам не нужно дублирование минусов например
                if (i > 0) { // добавим проверку на то не является ли текущий коэффициент свободным. тут или i>0  или i==0
                    sb.append("x"); // прошли проверку --> добавим в объект строки x
                    if (i > 1) { // проверим теперь степень. уж не больше ли 1
                        sb.append("^").append(i); // и если больше, то добавим в объект строки значек возведения в степень и измерение степени из i
                    } // закроем проверку if
                } // закроем проверку if на бытие свободным членом
            } // закроем проверку на вообше обработку этого коэффициента
        } // конец цикла for
        System.out.println("P(x) = " + sb.toString()); //  преобразуем объект sb в обычную строку, добавим текст "P(x) = " и выведем результат в консоль
    } // конец метода print_results





    public static void main(String[] args) { // создадим метод main() который является точкой входа в программу. он находится в public scope, принадлежит классу, возвращает void      

        String input_type = "regular"; // Значение по умолчанию для переменной input_type
        int input_dimension = 5; // Значение по умолчанию для переменной input_dimension
        double input_sparsity = 0.3; // Значение по умолчанию для переменной input_sparsity


        Scanner scanner = new Scanner(System.in); // создадим объект scanner класса Scanner для считывания пользовательского ввода с клавиатуры

        System.out.println("Какой полином будем генерировать?\n" // Выведем для пользователя информацию о доступных вариантах выбора в программе
        + "[1] - regular\n"
        + "[2] - symmetric\n"
        + "[3] - ones\n"
        + "[4] - sparse\n"
        + "[ ] - по умолчанию (regular random до^5)");
 
        input_type = scanner.nextLine().toLowerCase(); // сохраним то что пользователь ввел в переменную input_type, предварительно приведя к lowercase. В общем то lowercase тут уже не нужен, и остался с момента когда тип полинома нужно было вбивать словом, но если былобы реальное коммерческое приложение то каждый пользовательский ввод должен быть отфильтрован во избежание вбивания туда кода вместо вариантов выбора.
        if (input_type.isEmpty()) { // условие на случай пустого пользовательского ввода
            input_dimension = random.nextInt(input_dimension) + 1; // сгенериуем случайное число, обозначающее степень полинома с помощью random.nextInt(max_dimension) и исключим возможность нулевой степени, добавив единицу. Запишем в поле dimension.
            System.out.println("Создание полинома..."); // Выведем информационное сообщение для пользователя
        } else if (input_type.equals("1")) { // условие на случай если пользователь ввел 1 и в переменную input_type записалось 1 и equal 1 == true
            System.out.println("Создание обычного полинома...");  // Выведем информационное сообщение для пользователя
            System.out.println("Введите максимальную степень полинома:"); // попросим пользователя ввести необходимое для работы конструктора значение
            input_dimension = scanner.nextInt(); // с помощью ранее созданного объекта класса Scanner и метода nextInt() считаем целое число, введенное пользователем и запишем в переменную input_dimension
        } else if (input_type.equals("2")) { // условие на случай если пользователь ввел 1 и в переменную input_type записалось 2 и equal 2 == true
            System.out.println("Создание симметричного полинома...");  // Выведем информационное сообщение для пользователя
            System.out.println("Введите максимальную степень полинома:");  // попросим пользователя ввести необходимое для работы конструктора значение
            input_dimension = scanner.nextInt(); // с помощью ранее созданного объекта класса Scanner и метода nextInt() считаем целое число, введенное пользователем и запишем в переменную input_dimension
        } else if (input_type.equals("3")) { // условие на случай если пользователь ввел 1 и в переменную input_type записалось 3 и equal 3 == true
            System.out.println("Создание единичного полинома..."); // Выведем информационное сообщение для пользователя
            System.out.println("Введите максимальную степень полинома:");  // попросим пользователя ввести необходимое для работы конструктора значение
            input_dimension = scanner.nextInt(); // с помощью ранее созданного объекта класса Scanner и метода nextInt() считаем целое число, введенное пользователем и запишем в переменную input_dimension
        } else if (input_type.equals("4")) { // условие на случай если пользователь ввел 1 и в переменную input_type записалось 4 и equal 4 == true
            System.out.println("Создание разреженного полинома..."); // Выведем информационное сообщение для пользователя
            System.out.println("Введите степень полинома:");  // попросим пользователя ввести необходимое для работы конструктора значение
            input_dimension = scanner.nextInt(); // с помощью ранее созданного объекта класса Scanner и метода nextInt() считаем целое число, введенное пользователем и запишем в переменную input_dimension
            System.out.println("Введите коэффициент разреженности (от 0.0 до 1.0):");  // попросим пользователя ввести необходимое для работы конструктора значение
            input_sparsity = scanner.nextDouble(); // с помощью ранее созданного объекта класса Scanner и метода nextInt() считаем число с плавающей точкой, введенное пользователем и запишем в переменную input_sparsity
        } else { // условие на случай непредусмотренного пользовательского ввода
            input_dimension = random.nextInt(input_dimension) + 1; // сгенериуем случайное число, обозначающее степень полинома с помощью random.nextInt(max_dimension) и исключим возможность нулевой степени, добавив единицу. Запишем в поле dimension.
            System.out.println("Создание полинома..."); // Выведем информационное сообщение для пользователя
        } // конец условий для консольного интерфейса
 
        Polynom polynom_for_lab_rab_6 = new Polynom(input_dimension, input_type, input_sparsity); // создадим новый объект random_polynom_for_lab_rab_6 используя ранее созданный конструктор Polynom. Передадим степень полинома 5 в конструктор.
        polynom_for_lab_rab_6.print_results(); // выведем результат на экран, используя заранее подготовленный метод print_results


        scanner.close(); // закроем объект класса Scanner, освободив ресурсы, связанные с вводом

    } // конец метода main
} // конец класса Polynom
