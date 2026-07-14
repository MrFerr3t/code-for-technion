public class Lion extends Animal{
    private static final int DOMINANCE = 4;
    public Lion(){
        super(DOMINANCE);
    }
    @Override
    public Lion clone() {
        return (Lion) super.clone();
    }

}


