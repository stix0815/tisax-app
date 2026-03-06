'use client';

import { motion } from 'framer-motion';
import { Mail, Phone, MapPin } from 'lucide-react';

export default function Contact() {
  return (
    <main className="min-h-screen bg-deep-navy pt-32 pb-20 px-4">
      <div className="max-w-4xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16"
        >
          <h1 className="text-5xl font-bold mb-6">
            <span className="gradient-text">Kontakt</span>
          </h1>
          <p className="text-xl text-cool-grey">
            Lassen Sie uns gemeinsam Ihre digitale Zukunft gestalten.
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
          {/* Contact Info */}
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="bg-navy/50 backdrop-blur-lg border border-steel-blue rounded-2xl p-8 space-y-6"
          >
            <h2 className="text-2xl font-semibold gradient-text mb-6">
              Kontaktdaten
            </h2>

            <div className="flex items-start gap-4">
              <Mail className="text-neon-cyan mt-1" size={24} />
              <div>
                <h3 className="font-semibold text-off-white mb-1">E-Mail</h3>
                <a
                  href="mailto:info@celyvium.de"
                  className="text-cool-grey hover:text-neon-cyan transition-colors"
                >
                  info@celyvium.de
                </a>
              </div>
            </div>

            <div className="flex items-start gap-4">
              <Phone className="text-electric-indigo mt-1" size={24} />
              <div>
                <h3 className="font-semibold text-off-white mb-1">Telefon</h3>
                <a
                  href="tel:+49"
                  className="text-cool-grey hover:text-electric-indigo transition-colors"
                >
                  +49 (0) XXX XXXXXXX
                </a>
              </div>
            </div>

            <div className="flex items-start gap-4">
              <MapPin className="text-vivid-purple mt-1" size={24} />
              <div>
                <h3 className="font-semibold text-off-white mb-1">Adresse</h3>
                <p className="text-cool-grey">
                  Celyvium GmbH
                  <br />
                  Straße XX
                  <br />
                  XXXXX Stadt
                </p>
              </div>
            </div>
          </motion.div>

          {/* Contact Form */}
          <motion.div
            initial={{ opacity: 0, x: 30 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="bg-navy/50 backdrop-blur-lg border border-steel-blue rounded-2xl p-8"
          >
            <h2 className="text-2xl font-semibold gradient-text mb-6">
              Nachricht senden
            </h2>

            <form className="space-y-4">
              <div>
                <label className="block text-off-white mb-2 text-sm">Name</label>
                <input
                  type="text"
                  className="w-full bg-deep-navy border border-steel-blue rounded-lg px-4 py-3 text-off-white focus:border-electric-indigo focus:outline-none transition-colors"
                  placeholder="Ihr Name"
                />
              </div>

              <div>
                <label className="block text-off-white mb-2 text-sm">E-Mail</label>
                <input
                  type="email"
                  className="w-full bg-deep-navy border border-steel-blue rounded-lg px-4 py-3 text-off-white focus:border-electric-indigo focus:outline-none transition-colors"
                  placeholder="ihre@email.de"
                />
              </div>

              <div>
                <label className="block text-off-white mb-2 text-sm">Nachricht</label>
                <textarea
                  rows={5}
                  className="w-full bg-deep-navy border border-steel-blue rounded-lg px-4 py-3 text-off-white focus:border-electric-indigo focus:outline-none transition-colors resize-none"
                  placeholder="Ihre Nachricht..."
                />
              </div>

              <button
                type="submit"
                className="w-full bg-brand-gradient text-deep-navy font-semibold py-3 rounded-lg hover:shadow-2xl hover:shadow-electric-indigo/50 transition-all duration-300"
              >
                Senden
              </button>
            </form>
          </motion.div>
        </div>
      </div>
    </main>
  );
}
