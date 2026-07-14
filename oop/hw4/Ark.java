public class Ark{
private SpeciesQueue<Animal> queue;
public Ark(){
    this.queue = new SpeciesQueue<>();
}
public void add(Animal animal){
    this.queue.add(animal);
}
public void enterToArk(){
    if(!this.queue.isEmpty()){
        this.queue.remove();
    }
}

public void enterAllToArk(){
    while (!this.queue.isEmpty()) {
        enterToArk();
    }
}
public void showQueue() {
        StringBuilder sb = new StringBuilder();
        boolean isFirst = true;
        
        for (Animal animal : animalsQueue) {
            if (!isFirst) {
                sb.append(", ");
            }
            sb.append(animal.toString());
            isFirst = false;
        }
        
        System.out.println(sb.toString());
    }
    
}