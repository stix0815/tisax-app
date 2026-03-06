import type { Metadata } from "next";
import "./globals.css";
import Navigation from "@/components/Navigation";
import Footer from "@/components/Footer";

export const metadata: Metadata = {
  title: "Celyvium GmbH - Work, weightless.",
  description: "Digitales Marketing neu gedacht. Mit KI, Automatisierung und datenbasierter Strategie bringen wir Ihre Marke in die Zukunft.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="de">
      <body>
        <Navigation />
        {children}
        <Footer />
      </body>
    </html>
  );
}
