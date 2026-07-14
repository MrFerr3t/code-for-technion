public class EmptyQueueException extends SpeciesQueueException {
    public EmptyQueueException() {
        super("The queue is empty.");
    }

    public EmptyQueueException(String message) {
        super(message);
    }

    public EmptyQueueException(String message, Throwable cause) {
        super(message, cause);
    }
}