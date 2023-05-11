package open_bootcamp;

public class ejercicios_tema_8{

    public static void main(String [ ] args) {
        Persona individuo = new Persona();

        individuo.setEdad(31);
        individuo.setNombre("Pedro");
        individuo.setTelefono(1313131313);

        System.out.println("El nombre de la persona es: " +individuo.getNombre());
        System.out.println("La edad de la persona es: " +individuo.getEdad());
        System.out.println("El telefono de la persona es: " +individuo.getTelefono());
    }
}


class Persona {
    private int edad;
    private String nombre;
    private int telefono;
    
    public void setEdad(int edad){
        this.edad = edad;
    }
    public int getEdad(){
        return this.edad;
    }
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public String getNombre(){
        return this.nombre;
    }
    public void setTelefono(int telefono){
        this.telefono = telefono;
    }
    public int getTelefono(){
        return this.telefono;
    }
}