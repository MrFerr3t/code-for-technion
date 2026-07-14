public abstract class Animal implements Comparable<Animal>, Cloneable{
    private int dominance;
    public Animal(int dominance){
        this.dominance = dominance;
    }
    public int getDominance(){
        return dominance;
    }

    @Override
    public Animal clone(){
        try{
            return super.clone(Animal);
        }
        catch(CloneNotSupportedException e) {
            return null;
        }
    }   
    @Override 
    public int compareTo(Animal other){
        return Integer.compare(this.dominance,other.dominance);
        
    }

    @Override
    public String toString() {
        return this.getClass().getSimpleName();
    }


}