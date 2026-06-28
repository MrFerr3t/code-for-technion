public class Circle extends Shape{

    int radius;
    public Circle(int radius){
        this.radius = radius;
    }

    public double area(){
        return this.radius * this.radius * Math.PI;
    }

    public double perimeter(){
        return 2 * this.radius * Math.PI;
    }

    public int getHeight(){
        return this.radius * 2;
    }

    public int getWidth(){
        return this.radius * 2;
    }
    private double getDistance(int x, int y){
        return Math.sqrt(pow(x - radius) + pow(y - radius));

    }
    @Override
    public String toString(){
        StringBuilder res = new StringBuilder("");
        for(int i = 0; i < radius * 2; i++){
            for(int j = 0; j < radius * 2; j++){
                if(getDistance(i,j) <= radius + 0.3){
                    res.append("  *");
                }
                else{
                    res.append("   ");
                }

            }
            res.append("  /n");
            
        }
        return res;
    }
    @Override
    public boolean equals(Object obj){
        if(this == obj) return true;
        if(obj == null) return false;
        if(obj.getClass() != this.getClass()) return false;
        Circle circle = (Circle) obj;
        return this.radius == circle.radius;
    }

}