public class Zebra extends Animal{
    private static final int DOMINANCE = 1;
    public Zebra(){
        super(DOMINANCE);
    }
    @Override
    public Zebra clone() {
        return (Zebra) super.clone();
    }

}