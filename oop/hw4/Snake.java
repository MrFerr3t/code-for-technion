public class Snake extends Animal{
    private static final int DOMINANCE = 2;
    public Snake(){
        super(DOMINANCE);
    }
    @Override
    public Snake clone() {
        return (Snake) super.clone();
    }
    

}