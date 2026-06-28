public class RightAngleTriangle extends Shape{
    int height;
    int width;
    public RightAngleTriangle(int height, int width){
        this.height = height;
        this.width = width;
    }
    public double area(){
        return height * width / 2.0;
    }
    public double perimiter(){
        return height + width + Math.sqrt(height * height + width * width);
    }
    
    public int getHeight(){
        return this.height;
    }

    public int getWidth(){
        return this.width;
    }

    @override
    public String toString(){
        StringBuilder res = new StringBuilder("");
        int star_count = 0;
        for(int i = 1; i <= height; i++){
            star_count = Math.max(1, ((int) ((double) i * base / height)));
            for(int j = 0; i < star_count; i++){
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
        RightAngleTriangle triangle = (RightAngleTriangle) obj;
        return this.height == triangle.height && this.width == triangle.width;
    }


}
