public class InvalidInputException extends SpeciesQueueException {
    public InvalidInputException() {
        super("Invalid input provided.");
    }

    public InvalidInputException(String message) {
        super(message);
    }

    public InvalidInputException(String message, Throwable cause) {
        super(message, cause);
    }
}