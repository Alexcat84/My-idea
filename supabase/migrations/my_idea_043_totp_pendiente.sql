-- my_idea_043_totp_pendiente.sql — AUD-09 M50: RE-ENROLAR NO DESARMA EL CANDADO.
--
-- Con el doble factor ya activo (por correo o por otra app), iniciar el alta de
-- un autenticador nuevo cambiaba two_factor_method y pisaba totp_secret ANTES de
-- verificar el primer código. Si el usuario abandonaba el QR, el desafío pedía
-- un autenticador que nunca configuró y solo entraba con un código de rescate.
--
-- totp_secret_pendiente guarda el secreto nuevo (cifrado por la app, igual que
-- totp_secret) mientras se verifica. Solo al verificar un código de ESE secreto
-- pasa a totp_secret, el método cambia a 'totp' y el pendiente se limpia. El
-- candado vigente no se toca hasta entonces. Interna como el resto de la tabla
-- (RLS sin policies, solo service_role).

ALTER TABLE public.user_seguridad ADD COLUMN IF NOT EXISTS totp_secret_pendiente text;

COMMENT ON COLUMN public.user_seguridad.totp_secret_pendiente IS
  'AUD-09 M50: secreto TOTP nuevo (cifrado AES-256-GCM por la app) en espera de su primer codigo; al verificar pasa a totp_secret.';
