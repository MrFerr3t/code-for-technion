import java.util.Iterator;
import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;

public class SpeciesQueue<E extends Comparable<E> & Cloneable> implements Iterable<E>, Cloneable {
private E[] queue;
private int size; 
public static final int START_SIZE = 10;
public SpeciesQueue(){
    this.queue = (E[]) new Comparable[START_SIZE];
    this.size = 0;
}

public void add(E element){
    if(element == null){
        throw new InvalidInputException("Caught InvalidInputException while adding null");
    }
    if(size == queue.length){
        resize();
    }
    int i = this.size - 1;
    while(i >= 0){
        int cmp = queue[i].compareTo(element);
        if(cmp < 0){
            queue[i + 1] = queue[i];
            i--;
        }
        else if(cmp == 0){
            if(queue[i].getClass().equals(element.getClass())){
                queue[i + 1] = queue[i];
                i--;
            }
            else{
                int classCmp = queue[i].getClass().getName().compareTo(element.getClass().getName());
                if(classCmp < 0){
                    queue[i + 1] = queue[i];
                    i--;
                }
                else{
                    break;
                }
            }
            } 
        else{
            break;
        }
    }
    queue[i + 1] = element;
    this.size++;
}


public E remove(){
    if(isEmpty){
        throw new EmptyQueueException("Caught EmptyQueueException while removing from empty queue");
    }
    E head = queue[0];
    for(int i = 1; i < this.size; i++){
        queue[i - 1] = queue[i];
    }
    queue[this.size - 1] = null;
    return head;
}

public E peek(){
    if(this.size == 0){
        throw new EmptyQueueException("cannot peek at element from empty queue");
    }
    return queue[0];
}
public int size(){
    return this.size;
}
public boolean isEmpty(){
    return this.size == 0;
}

private void resize(){
    E[] newQueue = (E[]) new Comparable[queue.length * 2];
    for(int i = 0; i < queue.length; i++){
        newQueue[i] = queue[i];

    }
    queue = newQueue;
}
@Override
public SpeciesQueue<E> clone(){
    try {
        SpeciesQueue<E> clonedQueue = (SpeciesQueue<E>) super.clone();
        clonedQueue.queue = (E[]) new Comparable[this.queue.length];
        
        for (int i = 0; i < this.size; i++) {
            if (this.queue[i] != null) {
                try {
                    Method cloneMethod = this.queue[i].getClass().getMethod("clone");
                    clonedQueue.queue[i] = (E) cloneMethod.invoke(this.queue[i]);
                } catch (NoSuchMethodException | IllegalAccessException | InvocationTargetException e) {
                    return null; 
                }
            }
        }
        return clonedQueue;
    } catch (CloneNotSupportedException e) {
        return null;
    }
}

@Override
public Iterator<E> iterator() {
    return new Iterator<E>() {
        private int currentIndex = 0;

        @Override
        public boolean hasNext() {
            return currentIndex < size;
        }

        @Override
        public E next() {
            return queue[currentIndex++];
        }
    };
}


}
