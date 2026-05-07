function Toast({ toast, onClose }) {
  if (!toast) {
    return null;
  }

  return (
    <div className={`toast toast-${toast.type || "info"}`} role="status" aria-live="polite">
      <div className="toast-copy">
        <div className="toast-title">{toast.title}</div>
        <div className="toast-message">{toast.message}</div>
      </div>

      <button className="toast-close" type="button" onClick={onClose} aria-label="Close toast">
        x
      </button>
    </div>
  );
}

export default Toast;
