import type { Metadata } from "next";
import "./globals.css";
import { Providers } from "./providers";

// TODO: Fix next/font issue on Windows - temporarily use CSS variable
// const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });

export const metadata: Metadata = {
  title: "Terrabyte Academy",
  description: "Nigeria's Premier Technology Learning Platform",
  keywords: ["LMS", "online learning", "tech courses", "cybersecurity", "data science", "Nigeria"],
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-[#03091A] text-white antialiased">
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
