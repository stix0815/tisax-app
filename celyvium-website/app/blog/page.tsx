'use client';

import { motion } from 'framer-motion';

export default function Blog() {
  return (
    <main className="min-h-screen bg-deep-navy pt-32 pb-20 px-4">
      <div className="max-w-7xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center"
        >
          <h1 className="text-5xl font-bold mb-6">
            <span className="gradient-text">Blog</span>
          </h1>
          <p className="text-xl text-cool-grey max-w-3xl mx-auto mb-12">
            Insights, Trends und Know-how aus der Welt des digitalen Marketings.
          </p>

          <div className="bg-navy/50 backdrop-blur-lg border border-steel-blue rounded-2xl p-12">
            <p className="text-cool-grey text-lg">
              Der Blog wird bald mit Sanity CMS integriert.
              <br />
              Hier erscheinen dann Artikel zu KI, Automatisierung, Social Media und digitaler Strategie.
            </p>
          </div>
        </motion.div>
      </div>
    </main>
  );
}
