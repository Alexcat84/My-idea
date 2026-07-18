import { Suspense } from "react";
import { TusNumeros } from "@/app/ui/TusNumeros";

export default async function PaginaNumeros({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  return (
    <Suspense>
      <TusNumeros projectId={id} />
    </Suspense>
  );
}
