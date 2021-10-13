
public class Pilha<T>{
    T [] S;
    int top;

    public Pilha(int max){
        this.S = new T[max];
        this.top = -1;
    }

    boolean estaVazia(){
        return top==-1;
    }

    // PUSH
    void empilheirar(int x){
        top = top +1;
        S[top] = x;
    }

    // POP
    int desempilheirar() throws Exception{
        if(estaVazia()) throw new Exception(); 
        else{
            top = top -1;
            return S[top+1];
        }
    }


    public static void main(String[] args) {
        Pilha p = new Pilha(10);
        p.empilheirar(10);
        p.empilheirar(3);
        p.empilheirar(9);
        try {
            p.desempilheirar();
        } catch (Exception e) {
            e.printStackTrace();
        }
        p.empilheirar(30);
       System.out.println(); 
    }
}