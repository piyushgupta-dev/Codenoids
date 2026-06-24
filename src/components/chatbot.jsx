import { useState, useRef, useEffect } from "react";

const Chatbot = () => {
const [input, setInput] = useState("");
const [loading, setLoading] = useState(false);

const [messages, setMessages] = useState([
{
sender: "bot",
text: "Hello! How can I help you today?",
},
]);

const messagesEndRef = useRef(null);

useEffect(() => {
messagesEndRef.current?.scrollIntoView({
behavior: "smooth",
});
}, [messages]);

const handleSend = async () => {
if (!input.trim() || loading) return;

const userMessage = input;

setMessages((prev) => [
  ...prev,
  {
    sender: "user",
    text: userMessage,
  },
]);

setInput("");
setLoading(true);

try {
  const response = await fetch(
    "http://localhost:8000/chat",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message: userMessage,
      }),
    }
  );

  const data = await response.json();

  console.log("Response Status:", response.status);
  console.log("Response Data:", data);

  setMessages((prev) => [
    ...prev,
    {
      sender: "bot",
      text: data.response
  .replace(/\*\*/g, "")
  .replace(/\*/g, ""),
    },
  ]);
} catch (error) {
  console.error(error);

  setMessages((prev) => [
    ...prev,
    {
      sender: "bot",
      text: "Failed to connect to backend.",
    },
  ]);
} finally {
  setLoading(false);
}

};

return ( <div className="w-full h-full flex justify-center"> <div className="w-full max-w-5xl h-[80vh] bg-white rounded-3xl shadow-xl overflow-hidden flex flex-col">

    {/* Header */}
    <div className="bg-indigo-600 text-white px-6 py-4 flex items-center gap-3">
      <div className="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center text-xl">
        🤖
      </div>

      <div>
        <h1 className="font-semibold text-lg">
          AI Assistant
        </h1>
        <p className="text-xs text-indigo-100">
          Online
        </p>
      </div>
    </div>

    {/* Messages */}
    <div className="flex-1 overflow-y-auto bg-slate-50 p-4 md:p-6 space-y-4">

      {messages.map((msg, index) => (
        <div
          key={index}
          className={`flex ${
            msg.sender === "user"
              ? "justify-end"
              : "justify-start"
          }`}
        >
          <div
            className={`max-w-[80%] p-4 rounded-2xl whitespace-pre-wrap break-words ${
              msg.sender === "user"
                ? "bg-indigo-600 text-white rounded-br-md"
                : "bg-white text-gray-700 rounded-bl-md shadow-sm"
            }`}
          >
            {msg.text}
          </div>
        </div>
      ))}

      {loading && (
        <div className="flex justify-start">
          <div className="bg-white text-gray-700 p-4 rounded-2xl rounded-bl-md shadow-sm">
            Thinking...
          </div>
        </div>
      )}

      <div ref={messagesEndRef}></div>
    </div>

    {/* Input */}
    <div className="border-t bg-white p-4">
      <div className="flex gap-2">

        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          className="flex-1 px-4 py-3 border border-gray-300 rounded-xl outline-none focus:ring-2 focus:ring-indigo-500"
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleSend();
            }
          }}
        />

        <button
          onClick={handleSend}
          disabled={loading}
          className="bg-indigo-600 hover:bg-indigo-700 disabled:bg-gray-400 text-white px-5 py-3 rounded-xl font-medium transition"
        >
          {loading ? "..." : "Send"}
        </button>

      </div>
    </div>

  </div>
</div>

);
};

export default Chatbot;
