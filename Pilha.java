
public class Pilha{
    int [] S;
    int top;

    public Pilha(int max){
        S = new int[max];
        top = -1;
    }

    boolean estaVazia(){
        return top==-1;
    }

    // PUSH
    void inserir(int x){
        top = top +1;
        S[top] = x;
    }

    // POP
    int remover() throws Exception{
        if(estaVazia()) throw new Exception(); 
        else{
            top = top -1;
            return S[top+1];
        }
    }


    public static void main(String[] args) {
        Pilha p = new Pilha(10);
        p.inserir(10);
        p.inserir(3);
        p.inserir(9);
        try {
            p.remover();
        } catch (Exception e) {
            e.printStackTrace();
        }
        p.inserir(30);
       System.out.println(); 
    }
}