"use client";
import { useState } from "react";
import { useCourses } from "@/hooks/useCourses";
import CourseCard from "@/components/courses/CourseCard";
import CourseFilter from "@/components/courses/CourseFilter";

export default function CoursesPage() {
  const [filters, setFilters] = useState<Record<string, string>>({});
  const [search, setSearch] = useState("");
  const { data, isLoading } = useCourses({ ...filters, ...(search ? { search } : {}) });
  return (
    <div className="min-h-screen bg-[var(--bg)]">
      <div className="max-w-7xl mx-auto px-6 py-12">
        <h1 className="text-4xl font-black text-[var(--text)] mb-2 tracking-tight">Explore Courses</h1>
        <p className="text-[var(--text)]/40 mb-8">Find the perfect course to advance your career</p>
        <div className="relative mb-8">
          <span className="absolute left-4 top-1/2 -translate-y-1/2 text-[var(--text)]/25">⌕</span>
          <input type="text" placeholder="Search courses..." value={search} onChange={e=>setSearch(e.target.value)} className="w-full bg-[var(--surface)]/20 border border-[var(--muted)]/20 focus:border-brand-500 text-[var(--text)] placeholder:text-[var(--text)]/20 rounded-xl pl-11 pr-4 py-3.5 text-sm outline-none transition-all"/>
        </div>
        <div className="flex gap-10">
          <div className="w-52 shrink-0"><CourseFilter filters={filters} onChange={setFilters}/></div>
          <div className="flex-1">
            {isLoading ? (
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">{[...Array(6)].map((_,i)=><div key={i} className="bg-[var(--surface)]/20 rounded-2xl h-64 animate-pulse"/>)}</div>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {data?.items?.map((c:any)=><CourseCard key={c.id} course={c}/>)}
                {!data?.items?.length && <p className="text-[var(--text)]/30 col-span-3 text-center py-20">No courses found matching your filters.</p>}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
