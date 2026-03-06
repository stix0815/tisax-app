'use client';

import Link from 'next/link';
import { Mail, Linkedin, Twitter, Instagram } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="bg-deep-navy border-t border-steel-blue/30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          {/* Company */}
          <div>
            <h3 className="text-lg font-semibold gradient-text mb-4">Celyvium</h3>
            <p className="text-cool-grey text-sm leading-relaxed">
              Work, weightless.
              <br />
              Digitales Marketing neu gedacht.
            </p>
          </div>

          {/* Links */}
          <div>
            <h3 className="text-lg font-semibold text-off-white mb-4">Unternehmen</h3>
            <ul className="space-y-2">
              <li>
                <Link href="/about" className="text-cool-grey hover:text-neon-cyan transition-colors text-sm">
                  Über uns
                </Link>
              </li>
              <li>
                <Link href="/services" className="text-cool-grey hover:text-neon-cyan transition-colors text-sm">
                  Leistungen
                </Link>
              </li>
              <li>
                <Link href="/blog" className="text-cool-grey hover:text-neon-cyan transition-colors text-sm">
                  Blog
                </Link>
              </li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h3 className="text-lg font-semibold text-off-white mb-4">Kontakt</h3>
            <ul className="space-y-2">
              <li>
                <Link href="/contact" className="text-cool-grey hover:text-neon-cyan transition-colors text-sm">
                  Kontakt
                </Link>
              </li>
              <li>
                <a href="mailto:info@celyvium.de" className="text-cool-grey hover:text-neon-cyan transition-colors text-sm flex items-center gap-2">
                  <Mail size={16} />
                  info@celyvium.de
                </a>
              </li>
            </ul>
          </div>

          {/* Social */}
          <div>
            <h3 className="text-lg font-semibold text-off-white mb-4">Folgen Sie uns</h3>
            <div className="flex gap-4">
              <a
                href="#"
                className="text-cool-grey hover:text-neon-cyan transition-colors"
                aria-label="LinkedIn"
              >
                <Linkedin size={24} />
              </a>
              <a
                href="#"
                className="text-cool-grey hover:text-electric-indigo transition-colors"
                aria-label="Twitter"
              >
                <Twitter size={24} />
              </a>
              <a
                href="#"
                className="text-cool-grey hover:text-vivid-purple transition-colors"
                aria-label="Instagram"
              >
                <Instagram size={24} />
              </a>
            </div>
          </div>
        </div>

        <div className="border-t border-steel-blue/30 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-cool-grey text-sm">
            © {new Date().getFullYear()} Celyvium GmbH. Alle Rechte vorbehalten.
          </p>
          <div className="flex gap-6 text-sm">
            <Link href="/impressum" className="text-cool-grey hover:text-neon-cyan transition-colors">
              Impressum
            </Link>
            <Link href="/datenschutz" className="text-cool-grey hover:text-neon-cyan transition-colors">
              Datenschutz
            </Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
