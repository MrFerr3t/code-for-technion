public class Tiger extends Animal {
    private static final int DOMINANCE = 4;
    public Tiger(){
        super(DOMINANCE);
    }
    @Override
    public Tiger clone() {
        return (Tiger) super.clone();
    }

}