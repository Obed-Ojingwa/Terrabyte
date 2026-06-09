"use client";
import { useQuery } from "@tanstack/react-query";
import api from "@/lib/api";
import { useAuthStore } from "@/store/authStore";
import StatCard from "@/components/dashboard/StatCard";
import { BookOpen, CheckCircle, Trophy, Award } from "lucide-react";

export default function StudentDashboard() {
  const { user } = useAuthStore();
  const { data: stats } = useQuery({ queryKey: ["student-stats"], queryFn: async () => (await api.get("/analytics/student/stats")).data });
  const { data: enrollments } = useQuery({ queryKey: ["my-enrollments"], queryFn: async () => (await api.get("/enrollments/me")).data });

  return (
    <div className="p-6 space-y-8 min-h-full bg-[var(--primary)]/90">
      <div className="flex items-center justify-between">
        <div><h1 className="text-2xl font-black text-[var(--text)] tracking-tight">Welcome back, {user?.first_name}!</h1><p className="text-[var(--text)]/40 text-sm mt-1">Here&apos;s your learning progress overview</p></div>
        <div className="w-10 h-10 rounded-full bg-[var(--primary)] flex items-center justify-center text-sm font-bold text-[var(--text)]">{user?.first_name?.[0]}{user?.last_name?.[0]}</div>
      </div>
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard label="Enrolled" value={stats?.enrolled ?? 0} icon={<BookOpen size={16}/>} color="blue" />
        <StatCard label="Completed" value={stats?.completed ?? 0} icon={<CheckCircle size={16}/>} color="green" />
        <StatCard label="Assignments" value={stats?.assignments ?? 0} icon={<Trophy size={16}/>} color="yellow" />
        <StatCard label="Certificates" value={stats?.certificates ?? 0} icon={<Award size={16}/>} color="purple" />
      </div>
      <div>
        <h2 className="font-bold text-[var(--text)] text-sm mb-4">Active Courses</h2>
        <div className="space-y-3">
          {enrollments?.items?.map((e: any) => (
            <div key={e.id} className="bg-[var(--surface)]/20 border border-[var(--muted)]/20 rounded-2xl p-4 flex items-center gap-4">
              <div className="w-12 h-12 rounded-xl bg-[var(--primary)]/20 flex items-center justify-center flex-shrink-0"><BookOpen size={20} className="text-[var(--text)]/800"/></div>
              <div className="flex-1 min-w-0">
                <p className="font-semibold text-[var(--text)] text-sm truncate">{e.course?.title}</p>
                <div className="flex items-center gap-2 mt-2">
                  <div className="flex-1 bg-[var(--surface)]/20 rounded-full h-1.5 overflow-hidden"><div className="bg-[var(--primary)] h-full rounded-full transition-all" style={{width:`${e.progress ?? 0}%`}}/></div>
                  <span className="text-[var(--text)]/40 xs">{e.progress ?? 0}%</span>
                </div>
              </div>
              <button className="text-xs bg-[var(--primary)]/10 hover:bg-[var(--primary)]/20 text-[var(--text)]/300 border border-[var(--muted)]/20 px-3 py-2 rounded-xl transition-all flex-shrink-0">Continue</button>
            </div>
          ))}
          {!enrollments?.items?.length && <p className="text-[var(--text)]/30 text-sm text-center py-8">No enrolled courses yet. <a href="/public/courses" className="text-[var(--primary)] hover:underline">Browse courses →</a></p>}
        </div>
      </div>
    </div>
  );
}
