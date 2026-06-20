import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import QueryInput from "../components/QueryInput";
import UploadPanel from "../components/UploadPanel";
import MetricsCards from "../components/MetricsCards";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-[#0B0F14] text-white">

      <Navbar />

      <div className="grid grid-cols-12 gap-6 p-6">

        <div className="col-span-3">
          <Sidebar />
        </div>

        <div className="col-span-9 space-y-6">

          <MetricsCards />

          <UploadPanel />

          <ChatWindow />

          <QueryInput />

        </div>
      </div>
    </div>
  );
}