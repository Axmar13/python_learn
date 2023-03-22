package open_bootcamp;
import java.util.Scanner;

public class Main{

    public static void main(String [ ] args) {
        int numeroIf = 0;
        int numeroWhile = 0;
        if (numeroIf == 0){
            System.out.println("La variable numeroIf es igual a 0.");
        }else if (numeroIf > 0){
            System.out.println("La variable numeroIf es mayor que 0.");
        }else {
            System.out.println("La variable numeroIf es menor que 0.");
        }

        while (numeroWhile < 3){
            System.out.println(numeroWhile);
            numeroWhile++;
        }
        do {
            System.out.println(numeroWhile);
            numeroWhile++;
        } while (numeroWhile < 3);

        for (int numeroFor = 0; numeroFor <= 3; numeroFor++){
            System.out.println(numeroFor);
        }

        String estacion;

        System.out.println ("Por favor introduzca una estación por teclado:");

        Scanner entradaEscaner = new Scanner (System.in);

        estacion = entradaEscaner.nextLine ();

        switch (estacion) {
            case "VERANO":
                System.out.println("La estación actual es: \"" + estacion +"\"");
                break;
            case "OTOÑO":
                System.out.println("La estación actual es: \"" + estacion +"\"");
                break;
            case "INVIERNO":
                System.out.println("La estación actual es: \"" + estacion +"\"");
                break;
            case "PRIMAVERA":
                System.out.println("La estación actual es: \"" + estacion +"\"");
                break;
            default:
                System.out.println("El valor de la variable no es una estación");
                break;
        }
    }

}