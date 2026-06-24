const AboutMe = () => {
  return (
    <div className="min-h-screen bg-slate-100 flex justify-center items-center p-6">
      <div className="bg-white shadow-xl rounded-2xl p-8 max-w-4xl w-full">

        <h1 className="text-4xl font-bold text-blue-600 mb-6">
          About Me
        </h1>

        <div className="space-y-4 text-lg text-gray-700">

          <p>
            <strong>Name:</strong> Piyush Gupta
          </p>

          <p>
            <strong>Education:</strong> B.Tech Computer Science Engineering
          </p>

          <p>
            <strong>University:</strong> Kurukshetra University
          </p>

          <p>
            <strong>Role:</strong> Founder of CampusXcelerate
          </p>

          <p>
            <strong>Skills:</strong> React, React Native, JavaScript,
            Node.js, Firebase, Git, GitHub, GenerativeAI
          </p>

          <p>
            <strong>Hackathons:</strong> IIT BHU HaXplore Finalist,
            Escape Da Vinci Finalist, SIH Participant
          </p>

          <p>
            Passionate about Agentic AI, Mobile Development,
            Problem Solving, and Building Real-World Products.
          </p>

        </div>

        <div className="mt-8">
          <a
            href="/Piyush_Gupta_Resume.pdf"
            download
            className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg transition"
          >
            Download Resume
          </a>
        </div>

      </div>
    </div>
  );
};

export default AboutMe;