public class Rectangle extends Shape {
    int width;
    int height;

    public Rectangle(int width, int height){
        this.width = width;
        this.height = height;
    }

    public double Area(){
        return this.width * this.height;
    }

    public double Perimeter(){
        return this.width * 2 + this.height * 2;
    }

    public int getHeight(){
        return this.height;
    }

    public int getWidth(){
        return this.width;
    }
    @Override
    public String toString(){
        StringBuilder res = new StringBuilder("");
        for(int i = 1; i <= height; i++){
            for(int j = 1; i <= width; i++){
                res.append("  *");
                
            }
            res.append("  /n");
        }
        return res.toString();
}
    @Override
    public boolean equals(Object obj){
        if(this == obj) return true;
        if(obj == null) return false;
        if(obj.getClass() != this.getClass()) return false;
        Rectangle rectangle = (Rectangle) obj;
        return this.height == rectangle.height && this.width == rectangle.width;
    }
}
