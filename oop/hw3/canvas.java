public class Canvas{
    Shape[][] shapes;
    int canvasHeight;
    int canvasWidth;

    public Canvas(int canvasHeight, int canvasWidth){
        this.shapes = new Shape[canvasHeight][canvasWidth];
        this.canvasHeight = canvasHeight;
        this.canvasWidth = canvasWidth;
    }
    public void addShape(Shape shape, int width, int height){
        this.shapes[height][width] = shape;
    }

    public void removeShape(int width, int height){
        this.shapes[height][width] = null;
    }

    public double getTotalArea(){
        double areaSum = 0;
        for (int i = 0; i < this.canvasHeight; i++){
            for (int j = 0; j < this.canvasHeight; j++){
                areaSum = areaSum + shapes[i][j].area();
            }
        }
        return areaSum;
    }

    public double getTotalPerimeter(){
        double perimeterSum = 0;
        for (int i = 0; i < this.canvasHeight; i++){
            for (int j = 0; j < this.canvasHeight; j++){
                perimeterSum = perimeterSum + shapes[i][j].perimiter();
            }
        }
        return perimeterSum;
    }

    @Override
    public boolean equals(Object obj){
        if(this == obj) return true;
        if(obj == null) return false;
        if(obj.getClass() != this.getClass()) return false;
        Canvas canvas = (Canvas) obj;
        if (this.canvasHeight != canvas.canvasHeight || this.canvasWidth != canvas.canvasWidth){
            return false;
        }
        for (int i = 0; i < this.canvasHeight; i++){
            for (int j = 0; j < this.canvasHeight; j++){
                if (!this.shapes[i][j].equals(canvas.shapes[i][j])){
                    return false;
                }
            }
        }
        return true;
    }

    @Override
    public String toString(){
        StringBuilder res = new StringBuilder("");
        int maxWidth = 0;
        for(int i = 0; i < canvasHeight; i++){
            for(int j = 0; j < canvasWidth; j++){
                if(shapes[i][j].getWidth() > maxWidth){
                    maxWidth = shapes[i][j].getWidth();
                }
            }
        }
        
        for(int i = 0; i < canvasHeight; i++){
            int maxHeight = 0;
            for(int j = 0; j < canvasWidth; j++){
                if(shapes[i][j].getHeight() > maxHeight){
                    maxWidth = shapes[i][j].getHeight();
                }
            }
            for(int k = 0; k < maxHeight; k++){
                for(int j = 0; j < canvasWidth; j++){
                    if(shapes[i][j] == null){
                        res.append("   ").repeat(maxWidth);
                    }
                    else{
                        if(shapes[i][j].getHeight() >= k){
                            String currLine = shapes[i][j].split("\n")[k];
                            res.append(currLine);
                        }
                        else{
                            res.append("   ").repeat(maxWidth);
                        }
                        
                    }
                }
                res.append("   ");
            }
            res.append("\n");
        }
        return res.toString();
    }

}