public class Monkey extends Animal{
private static final int DOMINANCE = 3;
    public Monkey(){
        super(DOMINANCE);
    }
    @Override
    public Monkey clone() {
        return (Monkey) super.clone();
    }

}